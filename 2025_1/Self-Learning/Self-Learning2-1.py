"""
사용자가 제곱미터(m²) 단위로 입력한 토지의 면적을 평방피트(ft²)와 에이커(ac)
단위로 변환해주는 프로그램을 작성

기준
1제곱미터 (m²) = 10.7639 평방피트 (ft²)
1에이커 (ac) = 4046.86 제곱미터 (m²)

조건
입력받은 면적이 음수일 경우, 변환 대신 "잘못된 입력입니다"를 출력합니다.
이를 위해 if 선택문을 활용
"""

#1 정의
def convert_to_feet(square_meters):
    total_feet = square_meters * 10.7639
    return total_feet

def convert_to_acres(square_meters):
    total_acreas = square_meters / 4046.86
    return total_acreas

#2 입력
square_meters = float(input("토지의 면적을 제곱미터(m²) 단의로 입력하세요: "))

#3 출력
if square_meters < 0:
    print("잘못된 입력입니다.")
else:
    feet_msg = convert_to_feet(square_meters)
    print(f"{square_meters}제곱미터는 {feet_msg}평방피트입니다.")
    acres_msg = convert_to_acres(square_meters)
    print(f"{square_meters}제곱미터는 {acres_msg}평방피트입니다.")
    