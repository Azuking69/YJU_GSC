"""
For 문을 사용하여 아래 학생들의 성적에 대한 총합, 평균, 학생 수를 
출력하는 프로그램을 작성
"""

#1 성적 정의
score = [99, 29, 30, 40, 20, 60]

#2 학생 수
students_count = len(score)

#3 총합 계산
score_sum = sum(score)

#4 평균 계산
score_avg = score_sum / students_count

#5 출력
print(f"학생 수: {students_count}, 총점: {score_sum}, 평균: {score_avg}")