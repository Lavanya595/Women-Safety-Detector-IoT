
# Women Safety Detector 

An IoT-based system using *Raspberry Pi, Touch Sensor, LED, and Twilio API*.  
When the sensor is triggered, the system:
- Turns on an *emergency LED* and rungs a buzzer to grab help from surroundings.
- Sends an *SMS alert* and call to a predefined contact making help exccessable asap.

---

## Features
- Touch sensor detects distress signal  
- Sends instant SMS alert using Twilio  
- Emergency LED warning for nearby people  
- Easy to extend (GPS tracking, cloud logging, etc.)

---
##Hardware Setup (IoT Pro Kit Connections)
Raspberry Pi (BCM pin mode)
Provides the processing and Python execution.
Touch Sensor
Connect VCC → 3.3V (Raspberry Pi pin 1).
GND → GND (Raspberry Pi pin 6).
OUT → GPIO17 (Pin 11).
LED
Connect Anode → GPIO27 (Pin 13) with a 220Ω resistor.
Cathode → GND.
Buzzer
Connect +ve → GPIO22 (Pin 15).
-ve → GND.

##  Tech Stack
- Python  
- RPi.GPIO (for Raspberry Pi hardware control) from IOT pro kit.
- Twilio API (for SMS and Call alerts)

---

##  How to Run
install all the dependencies like raspberry pi , twilio, python libraries etc.


**Future implementations
GPS module can be added to send live location to seek help from near by police, family, friends etc.

##Output

![iot_result](https://github.com/user-attachments/assets/de7d938d-5e39-4c88-8883-2e33e0d23e73)


