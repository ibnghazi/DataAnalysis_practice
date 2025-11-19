import numpy as np

# 0차원 배열 생성 -> 스칼라(Scalar). 축(Axis)이 없는 배열
def zero_dimension_arr():
    # 연산 일관성을 유지, 브로드캐스팅, 내부처리 구조를 통일하기 위해 NumPy에서는 스칼라도 배열로 취급함

    arr1 = [1,2,3]
    arr = np.array(55)

    print(arr)
    print(type(arr))
    print(arr.ndim) # 차원수
    print(arr.shape) # 배열 형태
  
    print(arr1)
    print(type(arr1))
    print(arr1.shape) # 배열 형태
    print(arr1.ndim) # 차원수
    

    # print(arr[0]) # 에러 발생함

# zero_dimension_arr()

# 1차원 배열 생성 -> 벡터(Vector). 축이 1개

def one_dimension_arr():
    arr = np.array([1,2,3,4,5])

    print(arr)
    print(type(arr))

    # 차원수
    # 배열 형태
    print(arr.ndim) # 차원수
    print(arr.shape) # 배열 형태
    
    # 0으로 채워진 배열 생성 : np.zeros(개수)
    # 0이 5개 들어있는 배열 생성
    zero_arr = np.zeros(5)
    print(zero_arr)
    print(zero_arr.dtype) # 요소의 데이터 타입

    # 1로 채워진 배열 생성 : np.ones(개수)
    # 1이 10개 채워져있는 배열 생성
    ones_Arr = np.ones(10)
    print(ones_Arr)
    print(ones_Arr.dtype)

    # 특정 범위 내의 숫자로 채워진 배열 생성
    # : np.arange(시작값, 끝값, 증가값)
    arange_arr = np.arange(1,10,1)
    print(arange_arr)
# one_dimension_arr()

# 2차원 배열 생성 -> 행렬(Matrix), 축 2개 (Axis 0: 행, 1: 열)
def two_dimension_arr():
    arr = np.array(
        [
            [1,2,3],
            [4,5,6]
        ]
    )
    print(arr)
    print(type(arr))
    print(arr.ndim)
    print(arr.shape)

    # 0으로 채워진 배열
    arr2 = np.zeros((3,4))
    print(arr2)
    print(type(arr2))
    print(arr2.ndim)
    print(arr2.shape)

    # 1로 채워진 배열 생성 => 2x2, np.ones((행,열))
    arr3 = np.ones((2,2))
    print(arr3)
    print(type(arr3))
    print(arr3.ndim)
    print(arr3.shape)

    arange_arr = np.arange(1,10).reshape(3,3)
    print(arange_arr)
    print(arange_arr.ndim)
    print(arange_arr.shape)
    print(arange_arr.dtype)

# two_dimension_arr()

# 3차원 배열 생성 -> 텐서(Tensor). 축이 3개 (Axis 0:깊이-면, 1: 행, 2: 열)
def three_dimension_arr():
    arr = np.array([
        [
            [1,2,3],
            [4,5,6]
        ],
        [
            [7,8,9],
            [10,11,12]   
        ]
    ])

    print(arr)
    print(type(arr))
    print(arr.ndim)
    print(arr.shape) # (2,2,3) -> 2개의 면, 2개의 행, 3개의 열


    # 0으로 채워서 배열 생성 : np.zeros()
    zeros_arr = np.zeros((2,3,4))
    print(zeros_arr)

    # 1로 채워서 배열 생성 : np.ones((면,행,열))
    ones_Arr = np.ones((1,2,3))
    '''
      [[[1,1,1],[1,1,1]]]
    '''
    print(ones_Arr)
three_dimension_arr()