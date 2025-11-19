'''
reshape()
  -배열 형태를 (차원,가로/세로) 원하는 형태로 바꿔주는 함수 (재배치)
  -배열 요소의 총 개수는 유지해야함 (절대 변화해선 x)
  - 한 축의 크기를 자동 계산하고자 할 경우 -1 사용 (단, -1은 한번만 사용)
''' 

import numpy as np

def reshape_1d_to_2d():
  arr = np.arange(12)
  print(arr)

  arr_2d_3x4 = arr.reshape(3,4)
  print(arr_2d_3x4)

  # 2x2x3 형태로 변경
  arr_3d = arr.reshape(2,2,3)
  print(arr_3d)

  arr_3d = arr.reshape(1,6,2)
  print(arr_3d)

  # auto(-1) 적용
  arr_3d = arr.reshape(3,2,-1)
  print(arr_3d)
# reshape_1d_to_2d()

def reshape_to_1d():
  arr = np.arange(12).reshape(3,4)
  print(arr)

  arr_1d = arr.reshape(-1)
  print(arr_1d)

  arr_3d = arr.reshape(3,2,2)
  print(arr_3d)

  arr_1d = arr_3d.reshape(-1)
  print(arr_1d)
  # => reshape(-1) : 1차원 배열로 변경해줌

  print('-'*20)
  # * flatten() : 1차원 배열로 변경. 복사본을 반환해줌
  arr_flat = arr_3d.flatten()
  print(arr_flat)

  # * ravel() : 1차원 배열로 변경. 뷰를 반환해줌
  arr_ravel = arr_3d.ravel()
  print(arr_ravel)

# reshape_to_1d()

def copy_and_view():
  # 원본 배열
  origin_arr = np.arange(6)

  print(f'origin array: {origin_arr}')

  print('*---------ravel----------*')
  ravle_arr = origin_arr.ravel()
  print(f'ravel array : {ravle_arr}')
  
  ravle_arr[0] = 999

  print(f'ravel array : {ravle_arr}')
  print(f'origin array: {origin_arr}')
  # 원본 배열의 데이터도 변경됨.

  origin_arr[0] = 0 #초기화

  print('*-----flatten*-----')
  flat_arr = origin_arr.flatten()
  print(f'flatten array: {flat_arr}')

  flat_arr[0] = 666

  print(f'flatten array: {flat_arr}')
  print(f'origin array: {origin_arr}')


  print('*----reshape-----------------*')
  reshape_arr = origin_arr.reshape(2,-1)
  print(f'reshape array : {reshape_arr}')

  # 데이터 0(0,0)을 다른값으로 변경함
  reshape_arr[0,0] = 444

  print(reshape_arr)
  print(origin_arr)
  # => 원본 배열도 변경됨. 메모리 공유

  '''
            뷰(ravel, reshape)                     복사(flatten)

  메모리    원본과 공유 (하나의 데이터)            새로운 메모리 공간에 복제(두 개의 독립된 데이터)
  수정      뷰를 수정하면 원본도 변경              복사본을 수정해도 원본은 유지
  속도      빠름(복사 과정이 불필요)               상대적으로 느림(복사 과정 포함)
  
  '''
copy_and_view()