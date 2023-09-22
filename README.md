# [프로그래머스 인공지능 데브코스 6기] Monthly Project #1

## 프로젝트 - 데이터 시각화 웹 페이지 만들기
분석할 데이터를 선정 후 EDA를 같이 만들어보고 웹 페이지로 시각화
&nbsp;
### 분석 주제 
  · 고객 유형과 각각의 지난 2년간 와인, 육류, 생선, 금 등에 지출한 금액에 따른 상관관계 분석<br>
  
### 개요
&nbsp;각 고객의 유형에 따른 소비 유형을 분석하는 것은 기업이 특정 대상 고객 기반으로 마케팅하는데 도움을 준다. 예를 들어, 원래 신제품 마케팅을 진행할 때 모든 고객을 위한 마케팅 비용이 발생한다. 하지만 이 데이터로 어느 고객이 어떤 제품을 살지 특정할 수 있다면, 특정 고객에게만 마케팅을 하여 효율적인 비용 관리를 할 수 있다. 그리고 각 고객 유형이 많이 산 제품에 따라 매장 측면에서도 어떤 제품을 더 많이 공급할 지 결정할 수 있다. 따라서 우리는 이러한 장점을 극대화하기 위해 각 고객 유형별 소비 패턴을 분석하는 것을 목적으로 둔다.
  
### 가설
  1. 고객 가구의 자녀 수에 따라 지난 2년간 과자에 지출한 금액이 차이가 있을 것이다.
  2. 고객의 결혼 상태에 따라 지난 2년간 육류, 생선에 지출한 금액이 차이가 있을 것이다.
  3. 고객의 연간 가구 소득에 따라 지난 2년간 금에 지출된 금액이 차이가 있을 것이다.
  4. 고객 가구의 자녀 수나 청소년 수가 높을 수록 불만 사항을 제기한 경우가 비례할 것이다.

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
