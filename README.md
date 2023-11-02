## 전북대학교 학습도서관 옥상 AWS 기상대 기상자료 수집

---

* 학습도서관 옥상 AWS를 1시간 간격으로 업데이트 되며, 1분 단위로 로깅됩니다.

### 사용법

* 파일 다운로드
```
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
