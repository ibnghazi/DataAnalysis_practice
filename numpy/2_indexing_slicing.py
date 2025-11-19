import numpy as np

def practice_1d():
  # 1차원 배열 생성 -> [10,20,30,40,50,60]
  arr = np.array([10,20,30,40,50,60])
  arr2 = np.arange(10,61,10)
  arr3 = [10,20,30,40,50,60]

  print('1D')
  print(arr)
  print(arr2)
  print(arr3)

  print('indexing')
  print(arr[2])
  print(arr[-1])
  print(arr3[2])

  print('slicing')
  print(f'두번째 요소부터 네번째까지 : {arr[1:4:1]}')

  print(f'앞의 요소 3개 추출: {arr[:3]}')

  print(f'짝수번째 요소 추출: {arr[1::2]}')

  print(f'역순으로 추출 {arr[-1::-1]}')

# practice_1d()

def practice_2d():
  # 3행 4열 형태로 1 ~ 12까지 데이터를 담아 생성
  arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
  print(arr)
  
  print(arr[1,2])
  print(arr[:2,2:])

  #배열에서 1,2,3,4 추출
  print(arr[:1,])
  # 배열에서 2,6,10을 추출
  print(arr[:,1])
  
# practice_2d()

def practice_3d():
  # 1~12데이터를 저장하는 3차원 배열 (2x3 배열이 2개)
  arr = np.arange(1,13).reshape(2,2,3)
  # print(arr)
  # print(ar_arr)

  # 데이터중 6 출력하기
  print(arr[0][1][2])

  # 7~12값을 추출하기
  print(arr[1,:,:])

  # 1,2,3 ,7,8,9 추출하기
  print(arr[:,:1,:])
  print(arr[:,0])
# practice_3d()

def practice_boolean_indexing():
  # 1차원 배열 생성
  arr = np.array([10,20,30,43,50,8])
  print(arr)

  # 30보다 큰 요소만 추출
  print(arr > 30)
  print(arr[arr > 30])

  # 2차원 배열 생성
  # 10~90까지의 9개의 데이터를 저장 (3x3), 간격: 10
  arr1 = np.arange(10,91,10).reshape(3,3)

  # 50 < x < 80 데이터만 추출
  result = print((50 < arr1) & (arr1 < 80))
  # => 각 조건은 소괄호로 묶어주고, and 연산은 & 기호를 사용해야함
  print(arr1[result])

  # 최대값 추출 : max()
  print(arr1.max())
  print(arr1[arr1 == arr1.max()])


practice_boolean_indexing()

