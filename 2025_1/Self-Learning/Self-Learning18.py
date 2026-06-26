"""
학생들의 점수 리스트가 주어졌을 때, 각 점수를 분류하고 분류된 점수들의 
평균을 계산하는 프로그램을 작성

다음과 같이 점수를 분류하세요:
• 90 이상: '우수’
• 70 이상 90 미만: '양호’
• 50 이상 70 미만: '보통’
• 50 미만: '미흡’

각 분류에 따른 점수의 평균을 계산하고, 분류된 점수 리스트와 각 분류의 평균
점수를 출력
"""

#학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

high_scores = []
good_score = []
middle_score = []
low_score = []

for i in scores:
    if i >= 90:
        high_scores.append(i) #+=の時は[i]にする
    elif 70 <= i < 89:
        good_score.append(i)
    elif 50 <= i < 69:
        middle_score.append(i)
    else:
        low_score.append(i)

print(f"우수: [{high_scores}] 평균: {(sum(high_scores) / len(high_scores))}")
print(f"양호: [{good_score}] 평균: {(sum(good_score) / len(good_score))}")
print(f"보통: [{middle_score}] 평균: {(sum(middle_score) / len(middle_score))}")
print(f"미흡: [{low_score}] 평균: {(sum(low_score) / len(low_score))}")