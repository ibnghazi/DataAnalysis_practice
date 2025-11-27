import requests
import pandas as pd
from dotenv import load_dotenv
import os
import math
import time

#---------------
load_dotenv()  #.env파일 불러오기

# * 공공데이터 포털 사이트에서 발급받은 서비스 키(인증키)
SERVICE_KEY=os.environ.get('SERVICE_KEY')

# * BASE URL
BASE_SERVICE_URL='https://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2'

# * 재무상태표 조회 API
API_PATH = 'getBs_V2'

REQUEST_URL = f'{BASE_SERVICE_URL}/{API_PATH}'
# print(REQUEST_URL)


# -----------------------------API 연동 테스트 ----------------------------------
# params = {
#   "numOfRows": "10",
#   "pageNo" : "1",
#   "resultType" : "json",
#   "serviceKey" : SERVICE_KEY,
#   "crno" : '1301110006246'  # 삼성전자 법인번호 - 전자공시시스템(Dart)에서 조회

# }

# response = requests.get(REQUEST_URL, params=params)
# data = response.json()
# # print(data)

# # 응답 데이터 추출 data.get('key값', {공백인경우 처리될 값})
# items = data.get('response', {}).get('body', {}).get('items',{}).get('item',[])

# # ---- 반복문 이용하여 출력
# for x in items:
#   print(x)
# -----------------------------API 연동 테스트 ----------------------------------

# * API 요청 후 수집된 데이터를 CSV 파일로 저장 ================================
def get_first_data():
  '''
    재무 상태표 API의 첫번째 데이터와 전체 건수를 반환해주는 함수
  '''
  params = {
  "numOfRows": "10",
  "pageNo" : "1",
  "resultType" : "json",
  "serviceKey" : SERVICE_KEY,
  "crno" : '1301110006246'  # 삼성전자 법인번호 - 전자공시시스템(Dart)에서 조회
  }
  
  response = requests.get(REQUEST_URL, params=params)
  data = response.json()  #딕셔너리 형태로 받을 수 있음. json -> dictionary
  totalCount = data.get('response',{}).get('body',{}).get('totalCount', 0) # 전체 건수
  items = data.get('response',{}).get('body',{}).get('items',{}).get('item',[]) # 조회한 데이터 목록
  print(totalCount)
  print(items)

  if data:
    return items,totalCount
  else:
    return [], 0

# def save_csv():


# data_list, totalCount = get_first_data()

# if totalCount > 0:
#   # CSV파일로 저장하기
#   save_filepath = 'financial_ss.csv'
#   df = pd.DataFrame(data_list)
#   df.to_csv(save_filepath, encoding='UTF-8')
#   print('파일 저장 끝')

# numOfRows : 10, totalCount : 172 -> math.ceil(totalCount / numOfRows) 올림처리를 통해 전체페이지 수 구하기 -> 요청횟수 18번
# numOfRows : 100, totalCount : 172 --> 전체 페이지 수 : 2




# 전체 데이터를 수집하여 csv 파일로 저장
numOfRows = 10
pageNo = 1
items_sum = []

params = {
  "numOfRows": str(numOfRows),
  "pageNo" : str(pageNo),
  "resultType" : "json",
  "serviceKey" : SERVICE_KEY,
  "crno" : '1301110006246'  # 삼성전자 법인번호 - 전자공시시스템(Dart)에서 조회
  }

def get_new_params(pageNo):
  params["pageNo"] = str(pageNo)

  return params


response = requests.get(REQUEST_URL, params=params) 
data = response.json()  #딕셔너리 형태로 받을 수 있음. json -> dictionary
totalCount = data.get('response',{}).get('body',{}).get('totalCount', 0) # 전체 건수
count = math.ceil(totalCount/numOfRows)
print(f'반복횟수는 : {count}')

for i in range(count):
  time.sleep(1) #1초 지연 => 서버부하 방지
  if(data):
    items = data.get('response',{}).get('body',{}).get('items',{}).get('item',[])
    items_sum.extend(items)
    pageNo = pageNo+1
    params = get_new_params(pageNo)
    response = requests.get(REQUEST_URL, params=params)
    data = response.json()

if(items_sum) :
  save_filepath = 'financial_ss.csv'
  df = pd.DataFrame(items_sum)
  df.to_csv(save_filepath, encoding='UTF-8')
  print('파일 저장 끝')



