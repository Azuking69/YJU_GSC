import random

#1 사용자에게 메뉴를 출력
while True:
    menu = "----------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n-----------"
    print(menu)

#2 메뉴 선택택
    user_select = int(input("원하는 메뉴 번호를 입력하세요:"))


#3 구구단
#3-1 정의
    if user_select == 1:
        while True:
            def user_select_mul(start, end = None):
                if end is None:
                    for i in range(1, 10):
                        print(f"{start} x {i} = {i*start}")
                else:
                    for user_number in range(start, end + 1):
                        for i in range(1, 10):
                            print(f"{user_number} x {i} = {i*user_number}")
                        print()
    
#3-2  입력
            user_input = (input("출력할 구구단을 아래 형식으로 입력하세요(예:2, 2~5):"))

#3-3 종류 나누기 (int변환)
            if '~' in user_input:
                start, end = map(int, user_input.split('~'))
                if 2 <= start <= 9 and 2 <= end <= 9:
                    user_select_mul(start, end)
                    break
            elif '~' not in user_input:
                user_number = int(user_input)
                user_select_mul(user_number)
                break
            elif int(user_input) < 1 or 10 < int(user_input):
              print("2~9사이의 값으로 입력하세요")
  
#4 랜덤값 삼각형 출력
#4-1
    elif user_select == 2:
        high = int(input("삼각형의 높이 수를 입력하세요(2이상 3이하):"))
        while True:
            random_number1 = list(range(1, 10))
            random_number2 = list(range(10, 100))
            random_number3 = list(range(100, 1000))
            if high == 2:
                second_number = random.choice(random_number2)
                print(f" {random.choice(random_number1)}")
                print(f"{second_number}")
                break
            elif high == 3:
                second_number = random.choice(random_number2)
                third_number = random.choice(random_number3)
                print(f"  {random.choice(random_number1)}")
                print(f" {second_number}")
                print(f"{third_number}")
                break
            else:
                print("2 또는 3을 입력하세요")

#5 종료
    elif user_select == 3:
        print("프로그램을 종료합니다.")
        break

#6 Error
    else:
        print("1~3 사이의 값을 입력하세요")
