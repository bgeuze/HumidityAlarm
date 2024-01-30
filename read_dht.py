import Adafruit_DHT
import requests
import time
from twilio.rest import Client

# Twilio credentials
account_sid = 'AC4caed3c4927192e506375c3df2380fb9'
auth_token = '4f94211f07b2d826f85fb42b46e0521f'
twilio_phone_number = '+18544586850'
recipient_phone_number = '+31620911055'

# ThingSpeak parameters
apiKey = 'OROMH4Q8MVAU2Q35'
tempFieldID = '1'
humidityFieldID = '2'

# Sensor setup
sensor = Adafruit_DHT.DHT11
pin = 4

# Twilio client setup
client = Client(account_sid, auth_token)

def send_sms(message):
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print("SMS sent with message SID:", message.sid)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp: {0:0.1f} C'.format(temperature))
        print('Humidity: {0:0.1f} %'.format(humidity))

        # Check if humidity is not within desired range
        if humidity < 30 or humidity > 70:
            message = f"Alert: Humidity level is not optimal! Current humidity: {humidity}%"
            send_sms(message)

        # Update ThingSpeak records
        url = f'https://api.thingspeak.com/update?api_key={apiKey}&field{tempFieldID}={temperature}&field{humidityFieldID}={humidity}'
        response = requests.post(url)

        if response.status_code == 200:
            print('Data sent to ThingSpeak!')
        else:
            print('Failed to send data to ThingSpeak.')

    else:
        print('Failed to read data from sensor.')

    # Wait for 60 seconds before sending the next request
    time.sleep(60)
