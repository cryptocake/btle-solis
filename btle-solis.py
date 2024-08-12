from bluepy.btle import UUID, Peripheral, DefaultDelegate, BTLEException
import paho.mqtt.client as mqtt
import struct
import time
import json

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
# STOP EDITING #########################################################################

REGISTER_MAP = {
    # Advanced Information
    33071: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"dc_bus_voltage"},
    33072: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"busbar_half_voltage"},
    33079: {"value":None,"num":2,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"active_power"},
    33081: {"value":None,"num":2,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"Var","name":"reactive_power"},
    33083: {"value":None,"num":2,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"VA","name":"apparent_power"},
    33093: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.1,"unit":"℃","name":"inverter_temperature"},
    33105: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.001,"unit":"","name":"pf_actual_ajustment_value"},
    33136: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"llc_bus_voltage"},

    # Battery
    33111: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"bms_status"},
    33133: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"battery_voltage"},
    33134: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"battery_current"},
    33135: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"battery_current_direction"},
    33139: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"%","name":"soc_value"},
    33140: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"%","name":"soh_value"},
    33141: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"V","name":"battery_voltage_bms"},
    33142: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"battery_current_bms"},
    33143: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"battery_charging_current_limit"},
    33144: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"battery_discharging_current_limit"},
    33149: {"value":None,"num":2,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"batteryp_active_power"},
    33160: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"battery_type"},
    33161: {"value":None,"num":2,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"total_battery_charge_energy"},
    33163: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"today_battery_charge_energy"},
    33164: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"yesterday_battery_charge_energy"},
    33165: {"value":None,"num":2,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"total_battery_discharge_energy"},
    33167: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"today_battery_discharge_energy"},
    33168: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"yesterday_battery_discharge_energy"},
    33184: {"value":None,"num":2,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"kWh","name":"Total_Grid_Charging_Energy"},
    33208: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"underVoltage_protection_value"},
    33211: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"overVoltage_protection_value"},
    34345: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_Value"},
    34346: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"BatteryBMS_VoltageValue"},
    34347: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_State"},
    34348: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.001,"unit":"V","name":"BatteryBMS_MinVoltage"},
    34349: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.001,"unit":"V","name":"BatteryBMS_MaxVoltage"},
    34350: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"℃","name":"BatteryBMS_MinTemperature"},
    34351: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"℃","name":"BatteryBMS_MaxTemperature"},
    34352: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_MinLocation"},
    34353: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_MinVoltageCore"},
    34354: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_MaxLocation"},
    34355: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_MaxVoltageCore"},
    34356: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_MinLocationTemperature"},
    34357: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_MinTemperatureCore"},
    34358: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_MaxLocationTemperature"},
    34359: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_MaxTemperatureCore"},
    34360: {"value":None,"num":2,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"AH","name":"BatteryBMS_Capacity"},
    34362: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_NumberCycles"},
    34363: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_NumberParallel"},
    34364: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_NumberPacks"},
    34365: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"BatteryBMS_NumberModules"},

    # Battery Settings
    43009: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"current_operating_battery_model"},
    43011: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"%","name":"over_discharge_soc"},
    43012: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"maximum_charging_current"},
    43013: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"maximum_discharge_current"},
    43018: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"%","name":"strong_charge_soc"},
    43027: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":10,"unit":"W","name":"force_limit_current"},
    43110: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"energy_storage_control_switch"},
    43117: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"maximum_battery_charging_current_setting"},
    43118: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"maximum_battery_discharge_current_setting"},
    43348: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"awaken_voltage"},
    43349: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"s","name":"awaken_time"},
    43374: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":None,"unit":"","name":"output_port_control"},
    43376: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"s","name":"Awaken_Time_Setting"},
    43378: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":None,"unit":"","name":"G100_Manual_Fault_Clearing"},
    43481: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"%","name":"Overdischarge_Hysteresis_SOC"},
    43482: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"%","name":"battery_Healing_SOC"},
    43802: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"batteryDual_model"}
}

REGISTERS = {
    "33071": {"length": 35, "func_code": "04"},
    "33111": {"length": 50, "func_code": "04"},
    "33161": {"length": 48, "func_code": "04"},
    "33211": {"length": 1, "func_code": "04"},
    "34345": {"length": 21, "func_code": "04"},
    "43009": {"length": 19, "func_code": "03"},
    "43110": {"length": 9, "func_code": "03"},
    "43348": {"length": 2, "func_code": "03"},
    "43374": {"length": 5, "func_code": "03"},
    "43481": {"length": 2, "func_code": "03"},
    "43802": {"length": 1, "func_code": "03"},
}


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
        try:
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

            if TEST_MODE:
                print("Results:", REGISTER_MAP)
            else:
                publish_data_to_mqtt()

        except BTLEException as e:
            print(f"BTLE Error: {e}")
        finally:
            if TEST_MODE:
                print("Disconnected.")
            self.peripheral.disconnect()


if __name__ == "__main__":
    while not TEST_MODE:
        BtleSolis().run()
        time.sleep(INTERVAL)
    else:
        BtleSolis().run()
