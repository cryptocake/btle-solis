REGISTER_MAP_LITE = {
    # Advanced Information
    33079: {"value":None,"num":2,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"W","name":"active_power"},
    33081: {"value":None,"num":2,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"Var","name":"reactive_power"},
    33083: {"value":None,"num":2,"negative":1,"datamode":0,"datatype":1,"gain":1,"unit":"VA","name":"apparent_power"},
    33093: {"value":None,"num":1,"negative":1,"datamode":0,"datatype":1,"gain":0.1,"unit":"℃","name":"inverter_temperature"},

    # Battery
    33161: {"value":None,"num":2,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"total_battery_charge_energy"},
    33163: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"today_battery_charge_energy"},
    33164: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"yesterday_battery_charge_energy"},
    33165: {"value":None,"num":2,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"total_battery_discharge_energy"},
    33167: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"today_battery_discharge_energy"},
    33168: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.01,"unit":"kWh","name":"yesterday_battery_discharge_energy"},

    # Self-use Mode
    43141: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"timing_charging_current_setting"},
    43142: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"timing_discharge_current_setting"}
}

REGISTERS_LITE = {
    "33079": {"length": 15, "func_code": "04"},
    "33161": {"length": 8, "func_code": "04"},
    "43141": {"length": 2, "func_code": "03"}
}

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
    43802: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":1,"unit":"","name":"batteryDual_model"},

    # Self-use Mode
    43141: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"timing_charging_current_setting"},
    43142: {"value":None,"num":1,"negative":0,"datamode":0,"datatype":1,"gain":0.1,"unit":"A","name":"timing_discharge_current_setting"}
}

REGISTERS = {
    "33071": {"length": 35, "func_code": "04"},
    "33111": {"length": 50, "func_code": "04"},
    "33161": {"length": 48, "func_code": "04"},
    "33211": {"length": 1, "func_code": "04"},
    "34345": {"length": 21, "func_code": "04"},
    "43009": {"length": 19, "func_code": "03"},
    "43110": {"length": 9, "func_code": "03"},
    "43141": {"length": 2, "func_code": "03"},
    "43348": {"length": 2, "func_code": "03"},
    "43374": {"length": 5, "func_code": "03"},
    "43481": {"length": 2, "func_code": "03"},
    "43802": {"length": 1, "func_code": "03"},
}