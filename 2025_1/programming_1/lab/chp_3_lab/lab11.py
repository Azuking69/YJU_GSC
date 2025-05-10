#[사용자로부터 섭씨 온도를 입력받아 화씨 온도로 변환하는 함수를작성]
#[변환된 화씨 온도를 출력하는 프로그램을 작성]
#[화씨 온도는 섭씨 온도에 9/5를 곱한 후 32를 더해 계산]

#사용자로부터 섭씨 온도를 입력받아
celsius = int(input("섭씨 온도를 입력하세요:"))
#화씨 온도로 변환하는 함수를작성
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#변환된 화씨 온도를 출력
print(f"화씨 온도는 {convert_celsius_to_fahrenheit(celsius)}입니다.")
