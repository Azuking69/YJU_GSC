"""
사전 예약 시스템의 로직을 시뮬레이션하는 프로그램을 작성
사용자가 특정 이벤트의 사전 예약을 진행할 때, 사용자의 입력에 따라
예약 가능 여부를 판단하고 그에 따른 결과를 출력
"""

import sys
#1 사용자 입력
# 나이 입력
user_age = int(input("나이를 입력하세요: "))
# 행사 입력
event_code = input("예약하려하는 이벤트 코드를 입력하세요: ")
event_code_li = ["E1", "E2", "E3"]
if event_code not in event_code_li:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    sys.exit()

# 날짜 입력
event_date = int(input("원하는 예약 날짜를 입력하세요: "))
if event_date <= 0 or event_date >= 31:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    sys.exit()

#1 행사 정의
#E1 정의
if event_code == "E1":
    if user_age >= 18:
        print("예약이 완료되었습니다!")
    else:
        print("나이 제한으로 인해 예약할 수 없습니다.")
        
#E2 정의
elif event_code == "E2":
    if event_date % 2 ==0:
        print("예약이 완료되었습니다!")
    else:
        print("선택하신 날짜에는 예약할 수 없습니다.")
#E3 정의
elif event_code == "E3":
    #나이 제한
    if user_age >= 16:
        #날짜 제한
        if event_date % 7 == 0:
            print("예약이 완료되었습니다!")
        else:
            print("선택하신 날짜에는 예약할 수 없습니다.")
    else:
        print("나이 제한으로 인해 예약할 수 없습니다.")
