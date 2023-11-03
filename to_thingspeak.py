import urllib.request
from datetime import datetime, timedelta
import pandas as pd
import requests
import time
import os

def get_aws(year, month, day):
    api_url = f"http://203.239.47.148:8080/dspnet.aspx?Site=85&Dev=1&Year={year}&Mon={month}&Day={day}"
    response = requests.get(api_url)
    data = response.text
    data = data.strip().split('\n')
    df = pd.DataFrame([line.split(',') for line in data])

    temp = df.iloc[-1, 1]
    humid = df.iloc[-1, 2]
    Radn = df.iloc[-1, 6]
    wind_from = df.iloc[-1, 7]
    wind = df.iloc[-1, 13]
    rain = df.iloc[-1, 14]
    battery = df.iloc[-1, 16]
    # print(temp, humid, Radn, wind_from, wind, rain, battery)

    return temp, humid, Radn, wind_from, wind, rain, battery


def send_data(year, month, day):
    THINGSPEAK_URL = os.environ['THINGSPEAK_URL']

    api_key = THINGSPEAK_URL
    url = 'https://api.thingspeak.com/update'
    url = url + '?api_key=%s' % api_key
    url = url + '&field1=%s' % get_aws(year, month, day)[0]
    url = url + '&field2=%s' % get_aws(year, month, day)[1]
    url = url + '&field3=%s' % get_aws(year, month, day)[2]
    url = url + '&field4=%s' % get_aws(year, month, day)[3]
    url = url + '&field5=%s' % get_aws(year, month, day)[4]
    url = url + '&field6=%s' % get_aws(year, month, day)[5]
    url = url + '&field7=%s' % get_aws(year, month, day)[6]

    # print(url)
    urllib.request.urlopen(url)

def main():
    current_date = datetime.now()
    year = current_date.year
    month = str(current_date.month).zfill(2)
    day = str(current_date.day).zfill(2)

    get_aws(year, month, day)
    send_data(year, month, day)


if __name__=='__main__':
    main()
