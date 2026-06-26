"""
학생들의 세 과목 점수를 입력 받아 평균 점수를 계산하고, 평균에 따른 학점 등급을 
부여하는 프로그램
"""

#1 평균 정의
def calculate_avg(math_point, science_point, english_point):
    total_avg = (math_point + science_point + english_point) / 3
    return total_avg
    
#계산된 평균 점수를 사용하여 학점 등급을 결정
def score_class(avg_point):
    if avg_point >= 90:
        petern = "A"
        return petern

    elif avg_point >= 80:
        petern = "B"
        return petern

    elif avg_point >= 70:
        petern = "C"
        return petern

    elif avg_point >= 60:
        petern = "D"
        return petern
    
    else:
        petern = "F"
        return petern

#입력받은 점수들을 바탕으로 평균 점수를 계산
math_point = float(input("수학 점수를 입력하세요: "))
science_point = float(input("과학학 점수를 입력하세요: "))
english_point = float(input("영어 점수를 입력하세요: "))
calculate_avg(math_point, science_point, english_point)

avg_point = calculate_avg(math_point, science_point, english_point)
score_class(avg_point)

print(f"평균 점수는 {avg_point}점이고, 학점은 {score_class(avg_point)}입니다.")
