import Adafruit_DHT
import requests
import time

apiKey = 'OROMH4Q8MVAU2Q35'
tempFieldID = '1'
humidityFieldID = '2'

sensor = Adafruit_DHT.DHT11
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp: {0:0.1f} C'.format(temperature))
        print('Humidity: {0:0.1f} %'.format(humidity))

        url = f'https://api.thingspeak.com/update?api_key={apiKey}&field{tempFieldID}={temperature}&field{humidityFieldID}={humidity}'
        response = requests.post(url)

        if response.status_code == 200:
            print('Data sent to Dashboard!')
        else:
            print('Failed to send data to Dashboard.')

    else:
        print('Failed to read data from sensor.')

    # Wait for 60 seconds before sending the next request
    time.sleep(60)
