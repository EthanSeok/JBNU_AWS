## 전북대학교 학습도서관 옥상 AWS 기상대 기상자료 수집


* 학습도서관 옥상 AWS를 1시간 간격으로 업데이트 되며, 1분 단위로 로깅됩니다.

### 사용법

* 파일 다운로드
```
import requests

year = 2023 ## 연도
month = 11  ## 원하는 달

url = f"https://raw.githubusercontent.com/EthanSeok/JBNU_AWS/main/output/{year}_{month}.csv"
response = requests.get(url)
```

* 파이썬 pandas 활용 데이터프레임
```
import urllib.request
import pandas as pd

year = 2023
month = 11
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
![일교차](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/025a4c0d-0551-4b4b-84e2-d185bcfd10c3)

![시간별 습도](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/cd988f4e-7326-4bed-9020-a934c3a67966)

![일별 누적광량](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/dcd62ec7-4b4b-4308-b927-4647a918014a)

![일별 강수량](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/d54807d5-c3ed-46b6-b21b-b1d4208b8c96)

![일별 평균, 최대, 최저 기온](https://github.com/EthanSeok/JBNU_AWS/assets/93086581/f11fd396-be2e-4f82-a8e3-baee83b23e1d)
