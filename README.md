# HumidityAlarm

The **HumidityAlarm** project is designed to monitor humidity levels and send SMS notifications when the humidity levels exceed or fall below predefined thresholds. This feature proves particularly beneficial when working or spending extended periods in enclosed spaces like bedrooms or offices, ensuring optimal humidity levels conducive to productivity and well-being.

## Demo

https://github.com/bgeuze/HumidityAlarm/assets/51074721/fede5007-d403-4c4b-8704-92dfd4f8646c

The demo showcases the functionality of the **HumidityAlarm** system, including real-time monitoring (ThingSpeak) of humidity and temperature levels and SMS notifications triggered by high or low humidity.

## Process

### Problem Statement:

Recognizing the importance of maintaining optimal humidity levels, the **HumidityAlarm** project aims to provide users with a means to monitor humidity levels and receive alerts when levels deviate from the desired range.

### Implementation:

- Utilizing Adafruit_DHT library for humidity and temperature sensing.
- Integrating ThingSpeak for live data graph updates.
- Integrating SMS notification service using Twilio for real-time alerts.
- Continuous monitoring of humidity levels and triggering alerts based on predefined thresholds (currently set at 60 seconds).

### Challenges and Solutions:

- Ensuring compatibility with Raspberry Pi and proper sensor setup (using breadboard for easier connection).
- I ran into some coding problems where I used ChatGPT to help me solve the syntax errors.

## Requirements

- Raspberry Pi 3 model A+ (or above)
- Humidity and temperature sensor compatible with Adafruit_DHT library (I used the DHT11 sensor)
- Twilio account for SMS notification service
- Raspbian 11 (or above)
- Python 3.9.2 (or above)

## Installation

To set up the **HumidityAlarm** project, follow these steps:

1. **Raspberry Pi Setup:**
   - Install Raspbian 11 on your Raspberry Pi.
   - Ensure Python 3.9.2 is installed.

2. **Dependencies Installation:**
   - Install Adafruit_DHT library: `pip install Adafruit_DHT`
   - Install Twilio library: `pip install twilio`

3. **Configuration:**
   - Update the necessary parameters in the code, such as the ThingSpeak parameters and the Twilio API credentials and phone numbers.

## Usage

1. **Run the Program:**
   - Execute the main Python script to start monitoring humidity levels: `python3 read_dht.py`
   - Ensure the sensor is properly connected to the Raspberry Pi. (See image as reference)
     ![demoimagesensor](https://github.com/bgeuze/HumidityAlarm/assets/51074721/250f3372-a0bb-4f08-b991-33d143a6473a)

2. **Monitoring:**
   - The program continuously monitors humidity levels in real-time.
   - SMS notifications are triggered when humidity levels exceed or fall below predefined thresholds.

## Conclusion

The **HumidityAlarm** project provides an effective solution for monitoring humidity levels and receiving timely alerts. By leveraging Raspberry Pi and Twilio, users can stay informed about changes in humidity levels, allowing for prompt action and mitigation.

## References

- [Adafruit_DHT library documentation](https://learn.adafruit.com/dht)
- [Twilio API documentation](https://www.twilio.com/docs/)
- [Raspbian 11 installation guide](https://www.raspberrypi.org/software/)
- [DHT11 Temperature and Humidity Sensor](https://elektronicavoorjou.nl/product/dht11-temperatuur-en-vochtigheid-sensor/)
- [OpenAI ChatGPT](https://chat.openai.com)
