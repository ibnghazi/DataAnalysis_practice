# pandas/3_data_cleaning.py
import numpy as np
import pandas as pd

data = {
  'no': [1, 2, 3, 4, 1, 1,  
         5, 6, 7, 8, 9],
  'name': ['민성', '성빈', '승준', '민환', '수정', '민성', 
            '장훈', '재환', '지훈', '성호', '진형'],
  'age': [25, 30, 33, 20, np.nan, 20,
          np.nan, 147, 31, 27, 70],
  'score': [88.2, 66.9, np.nan, np.nan, 77.7, 20,
            92.5, 87.6, 67.8, 89.0, 72.5],
  'is_active': ['ok', 'nok', 'ok', 'nok', 'nok', 'ok',
                'ok', 'ok', 'ok', 'nok', 'ok']
}
# no : 중복 데이터 존재
# age, score : 결측치 포함

# DataFrame 객체 생성
df = pd.DataFrame(data)

def fillna_zero():
    '''
        결측치 데이터를 0으로 대체
    '''

    print(df)
    print('-'*30)

    # * 컬럼별 결측치 개수 확인
    print('* ---- 컬럼별 결측치 개수 ---- *')
    print(df.isnull().sum())

    # * 결측치 데이터를 다른 값으로 대체
    #   대상.fillna(대체할_값)

    #   age 컬럼의 결측치를 0으로 대체
    print('* --- 결측치 대체 전 --- *')
    print(df['age'])

    '''
    df['age'] = df['age'].fillna(0)
    print('* --- 결측치 대체 후 --- *')
    print(df['age'])
    '''

def fillna_median():
    '''
        결측치 데이터를 중앙값 대체
    '''
    # DataFrame 객체 생성
    # df = pd.DataFrame(data)

    # print(df)
    # print('-'*30)

    # age 컬럼의 중앙값 : median()
    print(df['age'].median())

    # --- age 컬럼의 결측치를 중앙값으로 대체 ---
    print(df)
    age_median = df['age'].median()
    df['age'] = df['age'].fillna(age_median)

    print('* --- 결측치 대체 후 --- *')
    print(df['age'])

def dropna_score():
    '''
       score 컬럼에 결측치가 있으면 
       해당 행을 제거
    '''
    # * 결측치 제거 : df.dropna(subset=[컬럼])
    print(df['score'])
    return df.dropna(subset=['score'])


def change_df(func):
    '''
        전역 변수 df가 참조했던 데이터를 바꾸므로 함수로 우회하여 처리
    '''
    global df
    df = func()

def print_score():
    print('* ========= score 결측치 제거 결과 ========= *')
    print(df)
    print(df['score'])
    print(df['score'].isnull().sum())
    print('* ======================================== *')

# * 중복값 처리 ---------------------------------
def drop_duplicated_data():
    print( df.duplicated(subset=['no', 'name']) )    # 중복 여부 확인

    # 중복 행 제거
    return df.drop_duplicates(subset=['no', 'name'], keep='last')

def print_drop_dupl_result():
    print('* ========= 중복 행 제거 결과 ========= *')
    print(df)
    print('* ======================================== *')

def transform_data_type():
    print('----- 데이터 타입 변환 ------------------ *')
    # ----- 데이터 타입 변환 ------------------ *
    #  대상.astype(변환할_타입)

    # is_active : 'ok' / 'nok' --> True / False

    print(df['is_active'])
    df['is_active'] = df['is_active'].map({'ok': True, 'nok': False}).astype(bool)

    print('---- 변환 후 데이터 ----')
    #print(df_drop['is_active'])

    # age 컬럼의 데이터를 float -> int 변환
    df['age'] = df['age'].astype(np.int64)
    #print(df_drop['age'])

    # * 모든 컬럼의 데이터타입... dtypes
    print(df.dtypes)


#  ---------- 불필요한 컬럼 제거 ------------------
#      drop()
# name 컬럼을 제거 -> 분석에서 사용되지 않는 항목
def drop_column():
    return df.drop(columns=['name'])

def last_print():
    print('* ---- 최종 데이터 프레임 ---- *')
    print(df)


# fillna_zero()
# 결측치 처리
fillna_median()
# dropna_score()
change_df(dropna_score)
print_score()

# 중복데이터 처리
# drop_duplicated_data()
change_df(drop_duplicated_data)
print_drop_dupl_result()

# 데이터 타입 변환
transform_data_type()

# 불필요한 컬럼 제거
# drop_column()
change_df(drop_column)
last_print()
