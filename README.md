# Zonneplan Nexus Home Battery Interface

This project provides a Python script to interface with the Nexus Home battery with Solis S6 eh3p10k-h-eu(zp) inverter. It was built specifically for Zonneplan customers and is currently a proof-of-concept (PoC) running on a Raspberry Pi with onboard Bluetooth positioned near the inverter.

## Features

- Communicates with the Nexus Home battery using Bluetooth Low Energy (BLE)
- Constructs and sends commands to the inverter and receives responses
- Parses the responses and prints the results

## Requirements

- A Raspberry Pi with onboard Bluetooth
- The `bluepy` Python library

## Installation

1. Clone this repository to your Raspberry Pi.
2. Install the `bluepy` library using pip: `pip install bluepy`

## Usage

Run the script with Python 3: `python3 btle-solis.py`

## Contributing

Feel free to join the development of this project. Any contributions you make are greatly appreciated.

## Future Plans

The goal is to turn this script into a Home Assistant HACS plugin someday. Stay tuned for updates!

## Community

Join the discussion about this project on Tweakers (https://gathering.tweakers.net/forum/list_messages/2258328).

## Disclaimer

This project is not officially associated with Zonneplan. Use at your own risk.
