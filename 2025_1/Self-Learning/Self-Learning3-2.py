"""
대학에서의 출석 점수는 여러분의 최종 성적 결정에 중요한 역할
영진전문대학에서는 출석 점수 만점을 20점으로 설정하고 있으며, 다음 기준에 따라 점수를 산정
"""

#1 정의
def calculate_attendance_score(hours_per_week, absence_hour, tardy_count):

#1-1 출석점수 계산법
    #총 수업 시간 계산법
    total_classes = hours_per_week * 15

    #지각 처리 규칙
    rate_count = tardy_count // 3

    #결석 처리 규칙
    attendance_score = rate_count + absence_hour

    #학점 미부여 (F처리)
    if attendance_score > total_classes / 4:
       return "F(학점 미부여)"
    #출석점수
    else:
        return f"{20 - (20 * attendance_score / total_classes):.2f}"

#2 입력
hours_per_week = int(input("주당 수업 시간을 입력하세요: ")) 
absence_hour = int(input("결석한 시간을 입력하세요: ")) 
tardy_count = int(input("지각 횟수를 입력하세요: ")) 

#3 출력
total_score = calculate_attendance_score(hours_per_week, absence_hour, tardy_count)
print(f"당신의 출석 점수는 {total_score}점입니다.")