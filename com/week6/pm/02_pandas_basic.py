import pandas as pd

#df = pd.read_json('./에어컨.json')
#print(df)
#print(df.head(5))
#print(df.tail(5))

#pandas Series
#Series 정의      0  1   2    3    4
#sData = pd.Series([1, 12, 53, 109, 28])
#print(sData)

#Series의 값 확인
#print(sData.values)

# Series의 index 확인
#print(sData.index)

# Series의 type 확인하기
#print(sData.dtypes)

# Index 변경하기
#sData = pd.Series([1, 12, 53, 109, 28], index=['a', 'b', 'c', 'd','e'])
#print(sData)
#print(sData['b'])

#Series의 index 확인
#print(sData.index)
'''
person_dict_list = [
    {'name': 'kim', 'age': 19, 'job': 'student'},
    {'name': 'jung', 'age': 25, 'job': 'teacher'},
    {'name': 'lee', 'age': 38, 'job': 'sales man'}
]
'''
#df = pd.DataFrame(person_dict_list)
#df = df[['name','age','job']]
#print(df)
#print(df['job'])
#df = pd.read_csv('./전국관광지정보표준데이터.csv', encoding = 'euc-kr')
#print(df)
#print(df.head(5))
#print(df['관광지명'])

'''
파일 읽고 / 쓰고 
파일 open >> 데이터 쓰고(pyhton -> json 변환 , dumps/loads) >> 파일 close
파일 읽기 / 쓰기 with ~ as dump/load
pandas 데이터 분석용 라이브러리 기초 (dataframe/ head, tail, index)

Naver API 다음 주 am/pm
셀레늄()
'''