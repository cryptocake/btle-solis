# Solis Bluetooth LE Interface

This project provides a Python script to interface with the Zonneplan Nexus Home battery with Solis S6 eh3p10k-h-eu(zp) inverter. It was built specifically for Zonneplan customers and is currently a proof-of-concept (PoC) running on a Raspberry Pi with onboard Bluetooth positioned near the inverter.

## Features

- Communicates with the Nexus Home battery using Bluetooth Low Energy (BLE)
- Constructs and sends commands to the inverter and receives responses
- Parses the responses and publishes them to an MQTT Broker

## Requirements

- A Raspberry Pi with onboard Bluetooth
- The `bluepy` and `paho-mqtt` Python libraries (see requirements.txt)
- Python 3.7 or newer

## Installation

1. Clone this repository to your Raspberry Pi
   
   `git clone https://github.com/cryptocake/btle-solis.git`
   

2. Run the following commands:
   ```bash
   cd ./btle-solis
   sudo apt install python3-venv
   python3 -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt
   ```
3. Find the MAC Address of your Solis inverter. The inverter's discoverable bluetooth name starts with `INV_`
   ```bash
   bluetoothctl
      power on
      agent on
      scan on
   ```
   
4. Trust the device and try to establish a connection
   ```bash
   bluetoothctl
      trust xx:xx:xx:xx:xx:xx
      connect xx:xx:xx:xx:xx:xx
   ```
   
5. If the connection failed, then try to press & hold the touch-button on the inverter for 5 seconds, until the button 
   starts flashing. Try to connect once again.
   

6. If connected successfully, disconnect and continue.
   ```bash
   bluetoothctl
      disconnect xx:xx:xx:xx:xx:xx
   ```
7. Edit the required values at the top of `btle-solis.py`
   ```python
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
   ```
8. Add the `mqtt.yaml` or `mqtt-lite.yaml` sensors to your Home Assistant configuration
   
   **LITE_MODE**: was added for people who already retrieve the Pylontech Force H3 information directly using the 
   Solarman Protocol. By using **LITE_MODE** you will only retrieve the most interesting values from the inverter.
   

9. Copy and paste the contents of `btle-solis.service` (do not forget to edit User and the correct path!)
   ```bash
   sudo nano /etc/systemd/system/btle-solis.service
   ```

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable btle-solis.service
   sudo systemctl start btle-solis.service
   ```


## Usage

Run the script with Python 3: `python3 btle-solis.py`

## Contributing

Feel free to join the development of this project. Any contributions you make are greatly appreciated.

## Future Plans

~~The goal is to turn this script into a Home Assistant HACS plugin someday. Stay tuned for updates!~~

## Community

Join the discussion about this project on Tweakers (https://gathering.tweakers.net/forum/list_messages/2258328).

## Disclaimer

This project is not officially associated with Zonneplan. Use at your own risk.
