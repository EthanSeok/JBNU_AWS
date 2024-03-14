## 전북대학교 학습도서관 옥상 AWS 기상대 기상자료 수집


* 학습도서관 옥상 AWS를 1시간 간격으로 업데이트 되며, 1분 단위로 로깅됩니다.

### 사용법

* 파일 다운로드
```
import requests

year = 2023
month = 11

url = f"https://raw.githubusercontent.com/EthanSeok/JBNU_AWS/main/output/{year}_{month}.csv"
response = requests.get(url)

if response.status_code == 200:
    with open(f"{year}_{month}.csv", 'wb') as file:
        file.write(response.content)
    print(f"파일 {year}_{month}.csv을 다운로드했습니다.")
else:
    print(f"파일 다운로드에 실패했습니다. 상태 코드: {response.status_code}")

```

* 파이썬 pandas 활용 데이터프레임
```
import urllib.request
import pandas as pd

year = 2023
month = '01'
url = f"https://raw.githubusercontent.com/EthanSeok/JBNU_AWS/main/output/{year}_{month}.csv"

response = urllib.request.urlopen(url)
df = pd.read_csv(response)
print(df)
```

<br>

### Thingspeak 로깅

`to_thingspeak.py`를 github action을 통해 10분 단위로 전송  
[https://thingspeak.com/channels/2328695](https://thingspeak.com/channels/2328695)

<img src="https://github.com/EthanSeok/JBNU_AWS/assets/93086581/0a3c7c23-9293-4673-ba89-2d93b643e102" height="700">


<br>

### 기상자료 분석
![daily_temperature_diff](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/86df1af9-0af5-4250-9664-afa2abfc1c85)

![humid](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/6e20d239-5861-4916-ac31-02a14c3f042e)

![radn_plot](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/505e9f9b-a447-4ff1-98c7-8a39c5a48a14)

![rainfall](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/ec77fcb9-0c62-4af8-9249-ac0dad7c1554)

![temp_total](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/84f59cb0-9734-4b0e-a2c8-c3906a7b1e8f)
