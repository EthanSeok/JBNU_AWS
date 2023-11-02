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

    timestamp = df.iloc[:, 0]
    temp = df.iloc[:, 1]
    humid = df.iloc[:, 2]
    Radn = df.iloc[:, 6]
    wind_from = df.iloc[:, 7]
    wind = df.iloc[:, 13]
    rain = df.iloc[:, 14]
    battery = df.iloc[:, 16]

    return temp, humid, Radn, wind_from, wind, rain, battery, timestamp

def save_to_csv(year, month, day, data):
    filename = f'./output/{year}'
    if not os.path.exists(filename):
        os.makedirs(filename)

    if not data.empty:
        if os.path.exists(f'{filename}/{month}.csv'):
            df = pd.read_csv(f'{filename}/{month}.csv')
            new_data = data.rename(columns={0:'Timestamp', 1:'Temp', 2:'Humid', 6:'Radn', 7:'Wind_degree', 13:'Wind', 14:'Rainfall', 16:'Battery'})
            df = pd.concat([df, new_data], ignore_index=True)
            df = df.drop_duplicates('Timestamp')
            df.to_csv(f'{filename}/{month}.csv', index=False)
        else:
            df = data.rename(columns={0:'Timestamp', 1:'Temp', 2:'Humid', 6:'Radn', 7:'Wind_degree', 13:'Wind', 14:'Rainfall', 16:'Battery'})
            df.to_csv(f'{filename}/{month}.csv', index=False)
    else:
        print("데이터가 비어있습니다.")

def main():
    current_date = datetime.now()
    year = current_date.year
    month = str(current_date.month).zfill(2)
    day = str(current_date.day).zfill(2)

    temp, humid, Radn, wind_from, wind, rain, battery, timestamp = get_aws(year, month, day)
    data = pd.concat([timestamp, temp, humid, Radn, wind_from, wind, rain, battery], axis=1)
    save_to_csv(year, month, day, data)

if __name__ == '__main__':
    main()
