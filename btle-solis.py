from bluepy.btle import UUID, Peripheral, DefaultDelegate, BTLEException
import struct


# Battery
rmap = {
    33045: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"V","name":"battery_voltage_bms2"},
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
    34200: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"%","name":"LG_Primary_battery_SOC"},
    34201: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"%","name":"LG_Primary_battery_SOH"},
    34202: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"LG_Primary_battery_Voltage_BMS"},
    34203: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"LG_Primary_battery_Current_BMS"},
    34204: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"LG_Primary_battery_max_Ch_power"},
    34205: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"LG_Primary_battery_max_Dis_power"},
    34206: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Primary_battery_DCDC_Main"},
    34207: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Primary_battery_DCDC_Test"},
    34208: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Primary_battery_BMS_high"},
    34209: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Primary_battery_BMS_low"},
    34210: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Primary_battery_Fault_ID"},
    34211: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Primary_battery_Results"},
    34212: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Primary_battery_Status"},
    34213: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"LG_Primary_battery_Power"},
    34216: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"%","name":"LG_Secondary_battery_SOC"},
    34217: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"%","name":"LG_Secondary_battery_SOH"},
    34218: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"LG_Secondary_battery_Voltage_BMS"},
    34219: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"LG_Secondary_battery_Current_BMS"},
    34220: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"LG_Secondary_battery_Max_Char_Power"},
    34221: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"LG_Secondary_battery_Max_Dis_Power"},
    34222: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Secondary_battery_DCDC_Main"},
    34223: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Secondary_battery_DCDC_Test"},
    34224: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Secondary_battery_BMS_high"},
    34225: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Secondary_battery_BMS_low"},
    34226: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Secondary_battery_Fault_ID"},
    34227: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Secondary_battery_Results"},
    34228: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"LG_Secondary_battery_Status"},
    34229: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"LG_Secondary_battery_Power"},
    34275: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"V","name":"Battery2_Voltage_BMS"},
    34276: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"Battery2_Current_BMS"},
    34278: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"%","name":"Battery2_SOC2"},
    34279: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"%","name":"Battery2_SOH2"},
    34281: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"Battery2_BMS2_Current_Limit"},
    34282: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"Battery2_BMS2_Discharge_Limit"},
    34288: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"Battery2Voltage_BMS"},
    34289: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"Battery2Voltage"},
    34290: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"Battery2Current"},
    34291: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"battery2urrentDirection"},
    34339: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"Battery2UnderVoltageValue"},
    34341: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"Battery2EqualizationVoltage"},
    34342: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"V","name":"Battery2OverVoltageValue"},
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
    34368: {"value":None,"num":2,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"Battery2ChargingDischargingPower"},
    34370: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"V","name":"Battery2_Voltage_BMS2"}
}


class NotificationDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        self.response = b''

    def handleNotification(self, cHandle, data):
        self.response += data


def calculate_checksum(command):
    command_bytes = bytearray.fromhex(command)
    crc = 0xFFFF
    for byte in command_bytes:
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
    return f"{command}{crc_hex}"


def construct_command(register_address: int, amount):
    command = f"FE04{register_address:04X}{amount:04X}"
    return calculate_checksum(command)


class BtleSolis:
    def __init__(self, mac_address, service_uuid_ffe0, char_uuid_ffe1, char_uuid_ffe2):
        self.mac_address = mac_address
        self.service_uuid_ffe0 = service_uuid_ffe0
        self.char_uuid_ffe1 = char_uuid_ffe1
        self.char_uuid_ffe2 = char_uuid_ffe2

        self.peripheral = None
        self.delegate = None
        self.char_ffe1_handle = None
        self.char_ffe2_handle = None
        self.results = {}

        self.registers = {
            "33045": {"length": 1},
            "33111": {"length": 50},
            "33161": {"length": 48},
            "33211": {"length": 1},
            "34200": {"length": 30},
            "34275": {"length": 17},
            "34339": {"length": 32}
        }

        self.connect()

    def connect(self):
        print("Connecting...")
        self.peripheral = Peripheral(self.mac_address)
        self.delegate = NotificationDelegate()
        self.peripheral.setDelegate(self.delegate)

        service_ffe0 = self.peripheral.getServiceByUUID(self.service_uuid_ffe0)
        self.char_ffe1_handle = service_ffe0.getCharacteristics(self.char_uuid_ffe1)[0]
        self.char_ffe2_handle = service_ffe0.getCharacteristics(self.char_uuid_ffe2)[0]

    def disconnect(self):
        print("Disconnected.")
        self.peripheral.disconnect()

    def send_command_and_get_response(self, command):
        command = bytearray.fromhex(command)
        self.char_ffe1_handle.write(command, withResponse=False)
        self.peripheral.writeCharacteristic(self.char_ffe2_handle.valHandle + 1, b"\x01\x00", withResponse=True)

        self.delegate.response = b''
        while True:
            if self.peripheral.waitForNotifications(0.5):
                continue
            break
        return self.delegate.response

    def parse_response(self, response, address, length):
        byte_count = response[2]
        data_start = 3
        data_end = data_start + byte_count
        data_field = response[data_start:data_end]

        i = 0
        while i < len(data_field):
            current_address = address + i // 2
            if i // 2 < length and current_address in rmap:
                num = rmap[current_address].get('num', 1)
                val = 0

                for j in range(num):
                    if i + 2 * j < len(data_field):
                        val = (val << 16) | struct.unpack('>H', data_field[i + 2 * j:i + 2 * j + 2])[0]

                rmap[current_address]['value'] = val * rmap[current_address].get('gain', 1)
                i += 2 * num
            else:
                i += 2

    def run(self):
        try:
            # Loop through each command
            for reg, info in self.registers.items():
                length = info["length"]
                command = construct_command(int(reg), length)

                print(f"Sending command for register {reg}...")
                try:
                    response = self.send_command_and_get_response(command)
                    self.parse_response(response, int(reg), length)
                except Exception as e:
                    print(f"Error retrieving data for register {reg}: {e}")

            print("Results:", rmap)

        except BTLEException as e:
            print(f"BTLE Error: {e}")
        finally:
            print("Disconnected.")
            self.peripheral.disconnect()


if __name__ == "__main__":
    # MAC address of the Solis S6 inverter
    address = "xx:xx:xx:xx:xx:xx"

    service_uuid_ffe0 = UUID("0000ffe0-0000-1000-8000-00805f9b34fb")
    char_uuid_ffe1 = UUID("0000ffe1-0000-1000-8000-00805f9b34fb")
    char_uuid_ffe2 = UUID("0000ffe2-0000-1000-8000-00805f9b34fb")

    main = BtleSolis(
        address,
        service_uuid_ffe0,
        char_uuid_ffe1,
        char_uuid_ffe2
    )

    main.run()
