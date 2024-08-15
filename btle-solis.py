from bluepy.btle import UUID, Peripheral, DefaultDelegate, BTLEException, BTLEDisconnectError
import paho.mqtt.client as mqtt
import struct
import time
import json
from registers import *

# EDIT HERE ############################################################################
MAC_ADDRESS = ""  # xx:xx:xx:xx:xx:xx MAC address of the Inverter

# UUIDs of the services and characteristics
SERVICE_UUID_FFE0 = "0000ffe0-0000-1000-8000-00805f9b34fb"
CHAR_UUID_FFE1 = "0000ffe1-0000-1000-8000-00805f9b34fb"
CHAR_UUID_FFE2 = "0000ffe2-0000-1000-8000-00805f9b34fb"

# MQTT Broker
MQTT_BROKER_IP = ""
MQTT_BROKER_PORT = 1883
MQTT_USERNAME = ""
MQTT_PASSWORD = ""

INTERVAL = 20  # Run this script every xx seconds.

# Set TEST_MODE to True if you want to test the data output inside your terminal first.
# In TEST_MODE you will not publish data to MQTT.
TEST_MODE = False

# Set LITE_MODE to True if you want to request minimal data from the inverter, see mqtt-lite.yaml.
LITE_MODE = False
# STOP EDITING #########################################################################

if LITE_MODE:
    REGISTER_MAP = REGISTER_MAP_LITE
    REGISTERS = REGISTERS_LITE


class NotificationDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        self.response = b''
        self.done = False

    def handleNotification(self, cHandle, data):
        self.response += data

        if len(self.response) >= 2:
            received_crc = self.response[-2:]
            calculated_crc = calculate_checksum(self.response[:-2].hex())

            if received_crc.hex().upper() == calculated_crc.upper():
                self.done = True
            else:
                self.done = False


def calculate_checksum(data):
    data_bytes = bytearray.fromhex(data)
    crc = 0xFFFF
    for byte in data_bytes:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1

    crc_high = (crc & 0xFF00) >> 8
    crc_low = (crc & 0x00FF)
    crc_hex = f"{crc_low:02X}{crc_high:02X}"
    return crc_hex


def construct_command(register_address: int, amount, func_code):
    command = f"FE{func_code}{register_address:04X}{amount:04X}"
    crc_hex = calculate_checksum(command)
    return f"{command}{crc_hex}"


def parse_response(response, address, length):
    byte_count = response[2]
    data_start = 3
    data_end = data_start + byte_count
    data_field = response[data_start:data_end]

    i = 0
    while i < len(data_field):
        current_address = address + i // 2
        if i // 2 < length and current_address in REGISTER_MAP:
            num = REGISTER_MAP[current_address].get('num', 1)
            val = 0

            # Combine the bytes to form the full value
            for j in range(num):
                if i + 2 * j < len(data_field):
                    val = (val << 16) | struct.unpack('>H', data_field[i + 2 * j:i + 2 * j + 2])[0]

            # Check if the value is signed
            if REGISTER_MAP[current_address].get('negative', 0) == 1:
                max_value = 1 << (16 * num)  # 2^16 for each register
                if val >= max_value // 2:  # If the highest bit is set, it's a negative number
                    val -= max_value  # Convert to signed by subtracting 2^(16 * num)

            gain = REGISTER_MAP[current_address].get('gain', 1)
            calculated_value = val * gain if gain is not None else val

            if isinstance(calculated_value, float) and calculated_value != int(calculated_value):
                calculated_value = round(calculated_value, 2)

            REGISTER_MAP[current_address]['value'] = calculated_value
            i += 2 * num
        else:
            i += 2


def publish_data_to_mqtt():
    client = mqtt.Client()
    if MQTT_USERNAME != "" and MQTT_PASSWORD != "":
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.connect(MQTT_BROKER_IP, MQTT_BROKER_PORT, 60)
    client.publish("home/btle-solis/data", json.dumps(REGISTER_MAP), retain=True)
    client.disconnect()


class BtleSolis:
    def __init__(self):
        self.peripheral = None
        self.delegate = None
        self.char_ffe1_handle = None
        self.char_ffe2_handle = None

    def connect(self):
        self.peripheral = Peripheral(MAC_ADDRESS)
        self.delegate = NotificationDelegate()
        self.peripheral.setDelegate(self.delegate)
        if TEST_MODE:
            print("Connected.")

        service_ffe0 = self.peripheral.getServiceByUUID(UUID(SERVICE_UUID_FFE0))
        self.char_ffe1_handle = service_ffe0.getCharacteristics(UUID(CHAR_UUID_FFE1))[0]
        self.char_ffe2_handle = service_ffe0.getCharacteristics(UUID(CHAR_UUID_FFE2))[0]

    def disconnect(self):
        if TEST_MODE:
            print("Disconnected.")
        self.peripheral.disconnect()

    def send_command_and_get_response(self, command, timeout=5):
        command = bytearray.fromhex(command)
        self.char_ffe1_handle.write(command, withResponse=False)
        self.peripheral.writeCharacteristic(self.char_ffe2_handle.valHandle + 1, b"\x01\x00", withResponse=True)

        self.delegate.response = b''
        self.delegate.done = False

        start_time = time.time()

        while not self.delegate.done:
            if time.time() - start_time > timeout:
                raise Exception(f"Timeout({timeout}) occurred while waiting on data.")
            self.peripheral.waitForNotifications(timeout)

        return self.delegate.response

    def run(self):
        # Loop through each command
        for reg, info in REGISTERS.items():
            length = info["length"]
            func_code = info["func_code"]
            command = construct_command(int(reg), length, func_code)

            if TEST_MODE:
                print(f"Sending command for register {reg}...")

            try:
                response = self.send_command_and_get_response(command)
                parse_response(response, int(reg), length)
            except Exception as e:
                print(f"Error retrieving data for register {reg}: {e}")
                continue

        if TEST_MODE:
            print("Results:", REGISTER_MAP)
            print("Disconnected.")
            self.peripheral.disconnect()
        else:
            publish_data_to_mqtt()

    def loop(self):
        while True:
            try:
                self.connect()
                while True:
                    self.run()
                    time.sleep(INTERVAL)
            except BTLEDisconnectError as e:
                print(f"BTLE Disconnected: {e}")
                print(f"Retrying after {INTERVAL} seconds...")
            except BTLEException as e:
                print(f"BTLE Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            finally:
                time.sleep(INTERVAL)


if __name__ == "__main__":
    if TEST_MODE:
        bs = BtleSolis()
        bs.connect()
        bs.run()
    else:
        BtleSolis().loop()
