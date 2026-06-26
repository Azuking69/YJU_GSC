#입력
selsius = int(input("현재 온도(썹씨)를 입력하세요: "))

#야외 활동 정의
def outdoor_sport():
    if 30 <= selsius:
        return '수영'
    elif 20 <= selsius:
        return '등산'
    elif 10 <= selsius:
        return '자전거 타기'
    else:
        return '스키'

#출력
print(f"\n현재 온도: {float(selsius)}도")
print(f"추천 활동: {outdoor_sport()}")