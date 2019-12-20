import time
import datetime
from sds011 import SDS011
import aqi
from influxdb import InfluxDBClient
import requests

DEV_PATH = '/dev/ttyUSB0'
url = 'https://airviewer.sun-asterisk.vn/api/secret/xxxx'


def mesure():
    sensor = SDS011(DEV_PATH, use_query_mode=True)
    # print('Sleep device...')
    sensor.sleep(sleep=True)  # Turn off fan and diode
    # print('Wake-up device...')
    sensor.sleep(sleep=False)  # Turn on fan and diode
    # print('Mesure for 30 secs...')
    time.sleep(30)  # Allow time for the sensor to measure properly
    # print('Query data...')
    result = sensor.query()
    # print('Sleep device...')
    sensor.sleep()  # Turn off fan and diode

    return result if result else (0, 0)


if __name__ == '__main__':
    pm25, pm10 = mesure()
    aqi = int(aqi.to_aqi([
        (aqi.POLLUTANT_PM25, pm25),
        (aqi.POLLUTANT_PM10, pm10),
    ]))
    print('Result: AQI: {}, PM2.5: {}, PM10: {}'.format(aqi, pm25, pm10))
    data = {'aqi': aqi,
            'pm10': pm10,
            'pm25': pm25}

    x = datetime.datetime.now()
    print (x)
    if aqi != 0:
        r = requests.post(url=url, data=data, verify=False)
    print (r.text)
