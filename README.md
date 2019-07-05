# SROS - Swarm Robotics Orchestration System
The system is intended to orchestrate automated systems 

## Worker Node (Client)

**IoT microNode**

For LoRaWAN (IoT cloud)
- Espressif ESP32-WROOM-32U
- Microchip RN2483 transceiver

For LoRa (private network)
- Heltec Wireless Stick 868MHz (https://www.amazon.co.uk/MakerHawk-Development-0-49inch-Bluetooth-Intelligent/dp/B07ML6528K/ref=sr_1_5?keywords=heltec&qid=1562141372&s=gateway&sr=8-5&th=1)

- uBlock MAX-7Q GPS module
- STM32 based flight controller

**ROS compadible - Semi-autonomous Node**

NAVIO2 Raspberry Pi Hat for Rovers, Copters and Planes (https://emlid.com/navio/)

## Gateway/Base station

### Gateway
- Heltec LoRa Gateway HT-M01 (https://www.amazon.co.uk/MakerHawk-Development-0-49inch-Bluetooth-Intelligent/dp/B07GTHTY6X/ref=sr_1_5?keywords=heltec&qid=1562141372&s=gateway&sr=8-5&th=1)
- RAK2245 LoRa Gateway (https://store.rakwireless.com/products/rak2245-pi-hat)

### Server

**Custom LoRa Gateway**
- Raspberry Pi 4 (https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
- LoRa Server OS (https://www.loraserver.io/)

## Orchestrator (Neural Network)

### Embedded Device
- Nvidia Jetson Nano (https://developer.nvidia.com/embedded/jetson-nano-developer-kit)

## Traffic Manager
Coming soon...

## Integration API
Coming soon...

## Web Interface
**Flight Controller**
- iNAV (https://github.com/iNavFlight/inav/wiki)
- CleanFlight (https://github.com/cleanflight/cleanflight)

**LoRa Gateway**
- LoRa Server Interface (https://www.loraserver.io/)
