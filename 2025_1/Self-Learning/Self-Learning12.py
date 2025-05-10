import random

user_choice = input("가위, 바위, 보 중 하나를 선택하세요:")

#난수를 생성하여 리스트에서 요소를 선택하는 방법

choice = ['가위', '바위', '보']
computer_choice = random.choice(choice)

print(f"컴퓨터의 선택: {computer_choice}")

#결과 출력
if user_choice == computer_choice:
    print("결과: 무승부입니다!")
elif (user_choice == "가위" and computer_choice == "바위") or\
     (user_choice == "바위" and computer_choice == "보") or\
     (user_choice == "보" and computer_choice == "가위"):
    print("결과: 당신이 이겼습니다!")
elif (user_choice == "가위" and computer_choice == "보") or\
     (user_choice == "바위" and computer_choice == "가위") or\
     (user_choice == "보" and computer_choice == "바위"):
      print("결과: 당신이 졌습니다!")
else:
    print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요")
    