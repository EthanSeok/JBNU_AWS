## 전북대학교 학습도서관 옥상 AWS 기상대 기상자료 수집

---

* 학습도서관 옥상 AWS를 1시간 간격으로 업데이트 되며, 1분 단위로 로깅됩니다.

### 사용법

```
year = 2023 ## 연도
month = 11  ## 원하는 달

url = f"https://raw.githubusercontent.com/EthanSeok/JBNU_AWS/main/output/{year}_{month}.csv"
response = requests.get(url)
```
