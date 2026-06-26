"""
여러분은 학생들의 점수 데이터를 분석하고, 점수에 따른 등급 분포를
텍스트 기반의 그래프로 시각화하는 프로그램을 작성

다음과 같이 점수를 분류하세요:
• 90 이상: 'A' 등급
• 80 이상 90 미만: 'B' 등급
• 70 이상 80 미만: 'C' 등급
• 60 이상 70 미만: 'D' 등급
• 60 미만: 'F' 등급

각 등급별로 학생 수를 계산하고, 등급별 학생 수를 '*' 문자를 사용하여
히스토그램 형태로 시각화하고 각 등급의 평균 점수도 계산하여 함께 출력

제약사항 없음. 파이썬에서 제공하는 모든 함수, 연산자 사용 가능
"""

#학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

scores_A = []
scores_B = []
scores_C = []
scores_D = []
scores_F = []

for i in scores:
    if i >= 90:
        scores_A.append(i)
    elif 80 <= i < 90:
        scores_B.append(i)
    elif 70 <= i < 80:
        scores_C.append(i)
    elif 60 <= i < 70:
        scores_D.append(i)
    else:
        scores_F.append(i)

#""" """（三重クォート）で改行できる
print(f"""등급 분포 및 평균 점수: 
A 등급: 평균 점수 = {(sum(scores_A)) / len(scores_A):.2f}
{"*" * len(scores_A)} ({len(scores_A)}명)
B 등급: 평균 점수 = {(sum(scores_B)) / len(scores_B):.2f}
{"*" * len(scores_B)} ({len(scores_B)}명)
C 등급: 평균 점수 = {(sum(scores_C)) / len(scores_C):.2f}
{"*" * len(scores_C)} ({len(scores_C)}명)
D 등급: 평균 점수 = {(sum(scores_D)) / len(scores_D):.2f}
{"*" * len(scores_D)} ({len(scores_D)}명)
E 등급: 평균 점수 = {(sum(scores_F)) / len(scores_F):.2f}
{"*" * len(scores_F)} ({len(scores_F)}명)
    """)