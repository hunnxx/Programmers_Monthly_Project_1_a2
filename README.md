# [프로그래머스 인공지능 데브코스 6기] Monthly Project #1

## 프로젝트 - 데이터 시각화 웹 페이지 만들기
분석할 데이터를 선정 후 EDA를 같이 만들어보고 웹 페이지로 시각화
&nbsp;
### 분석 주제 
고객 유형과 각각의 지난 2년간 와인, 육류, 생선, 금 등에 지출한 금액에 따른 상관관계 분석
&nbsp;
## 데이터셋
Kaggle - [Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)  
![Kaggle-Customer-Personality_Analysis_Dataset](images/customer_personality_analysis_dataset.png)


&nbsp;
## 환경 설정
프로젝트 GitHub Repository 다운로드(또는 클론)
```shell
git clone https://github.com/hunnxx/Programmers_Monthly_Project_1_a2.git
```
가상환경 생성
```shell
python -m venv <virtual_env_name>
```
가상환경 실행
```shell
# if linux or mac
source <virtual_env_name>/bin/activate
# if window
./<virtual_env_name>/Scripts/activate
```
Python 라이브러리 설치 `in /Programmers_Monthly_Project_1_a2`
```shell
pip install requirements.txt
```
Python 라이브러리 설치 확인
```shell
pip freeze
```

&nbsp;
## 프로젝트 실행
서버 실행 `in /Programmers_Monthly_Project_1_a2/monthly_proj_1`
```shell
python manage.py runserver
```
[프로젝트 결과물 확인](http://127.0.0.1:8000)
