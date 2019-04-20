# Pandas를 이용하여 엑셀의 성적표를 불러와 분석 해보자.
import pandas as pd
import matplotlib.pyplot as plt

#엑셀 파일 읽기
#ImportError: Install xlrd >= 1.0.0 for Excel support가 출력 될 경우 Settings >> project >> interpreter에서 xlrd를 설치한다.
df = pd.read_excel('./class_score.xlsx')

#print(df)

#각 학생별 총점과 평균 열을 추가
subjects = ['국어', '영어', '수학', '과학', '사회']
df['총점'] = df[subjects].sum(axis=1) # axis : {index (0), columns (1)} # 0은 행방향으로의 합(즉, 각 열의 합) # 1은 열방향으로의 합(즉, 각 행의 합)
df['평균']= df['총점'] / len(subjects)
#print(df)

#평균으로 정렬한다 (내림차순 정렬  ! 기본값은 오름처순 정렬이다.)
df.sort_values(['평균'], ascending=[False])

#print(df.sort_values(['평균'], ascending=[False]))

##시각화 각 학생별 평균 점수로 그래프를 그려보자
import matplotlib.pyplot as plt

## 한글 폰트가 깨질 경우..
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#df.plot.bar(x='이름',y='평균')
#df.plot.barh(x='이름',y='평균')
#plt.show()

#각 반별 점수 비교
ban_1 = df[df['반']==1]
ban_2 = df[df['반']==2]
ban_3 = df[df['반']==3]
#print(ban_1)

ban_1_avg = ban_1['평균'].sum() / len(ban_1.index)
ban_2_avg = ban_2['평균'].sum() / len(ban_2.index)
ban_3_avg = ban_3['평균'].sum() / len(ban_3.index)

#print("1반 평균 : ",ban_1_avg,"2반 평균 : ",ban_2_avg,"3반 평균 : ",ban_3_avg)

#각 1반 과학 과목 평균
ban_1_science_score_avg = ban_1['과학'].sum() / len(ban_1.index)
#print(ban_1)
#print(ban_1_science_score_avg)

#각 학생들 과목 점수 데이터 plot 그리기
df.plot.bar(x='이름',y=subjects)
plt.show()
