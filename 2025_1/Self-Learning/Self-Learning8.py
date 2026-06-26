#사용자로부터 현재 온도(섭씨)를 입력받습니다. 
temperature = int(input("현재 온도(섭씨)를 입력하세요:"))

#입력받은 온도에 따라, 적합한 야외 활동을 추천하는 프로그램을 작성
if 30 < temperature :
    print(f"현재 온도:{temperature}")
    print("추천 활동: 수영")

elif 20 < temperature < 29:
    print(f"현재 온도:{temperature}")
    print("추천 활동: 등산")

elif 10 <= temperature < 19:
    print(f"현재 온도:{temperature}")
    print("추천 활동: 자전거 타기")

elif temperature <= 9:
    print(f"현재 온도:{temperature}")
    print("추천 활동: 스키키")