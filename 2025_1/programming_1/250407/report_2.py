"""
비교 연산자와 논리 연산자를 사용하여, 학생의 점수를 기반으로
우수합격/합격/불합격 판정을 내리는 프로그램
"""

#1 입력 : 국어, 영어, 수학 점수 (int형)
native_language = int(input("국어 점수: "))
english = int(input("영어 점수: "))
math = int(input("수학 점수: "))

#2 평균 계산
total_avg = float(native_language + english + math) / 3

#3 and 조건을 활용한 판정 로직 구성
#3-1 '우수 합격': 평균이 90점 이상이고, 모든 과목이 80점 이상일 경우
if total_avg >= 90 and native_language >= 80 and english >= 80 and math >= 80:
    print_avg = "우수 합격"
#3-2 '합격': 평균이 70점 이상이고, 각 과목이 모두 40점 이상일 경우
elif total_avg >= 70 and native_language >= 40 and english >= 40 and math >= 40:
    print_avg = "합격"
#3-3 위 조건을 만족하지 못하면 '불합격'
else:
    print_avg = "불합격"

#4 출력 : 평균 점수(float)와 판정 결과
print(f"평균: {total_avg:.1f}점")
print(f"결과: {print_avg}")