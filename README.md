# SROS - Swarm Robotics Orchestration System
The system is intended to orchestrate automated systems 

## Drone Node (Worker Client)

**Parts/Components:**
For LoRaWAN (IoT cloud)
- Espressif ESP32-WROOM-32U
- Microchip RN2483 transceiver

For LoRa (private network)
- Heltec Wireless Stick 868MHz (https://www.amazon.co.uk/MakerHawk-Development-0-49inch-Bluetooth-Intelligent/dp/B07ML6528K/ref=sr_1_5?keywords=heltec&qid=1562141372&s=gateway&sr=8-5&th=1)

- uBlock MAX-7Q GPS module
- STM32 based flight controller

The nodes consist of an ESP32 based controller with an RN2483 transceiver.

## Gateway/Base station
**Parts/Components**

Custom LoRaWAN Gateway
- Raspberry Pi 4
- LoRa Server OS (Operating System)
- RAK2245 LoRa Gateway

Production
- Heltec LoRa Gateway HT-M01 (https://www.amazon.co.uk/MakerHawk-Development-0-49inch-Bluetooth-Intelligent/dp/B07GTHTY6X/ref=sr_1_5?keywords=heltec&qid=1562141372&s=gateway&sr=8-5&th=1)

## Orchestrator (Neural Network)
Coming soon...

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
