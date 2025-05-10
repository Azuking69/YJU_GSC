import random

#컴퓨터 인식된 선택
choice = ['가위', '바위', '보']


#전역
user_wins = 0
computer_wins = 0
draws = 0
rounds = 0

#결과 출력
while rounds < 3 and max(user_wins , computer_wins) < 2:
    #사용자로부터 가위, 바위, 보 중 하나를 입력받고
    user_choice = input("가위, 바위, 보 중 하나를 선택하세요:").strip()
     

#컴퓨터 인식된 선택     
    computer_choice = random.choice(choice)
    print(f"컴퓨터: {computer_choice}")


    if user_choice == computer_choice:
        draws += 1
        print(f"무승부! 현재 전적 : {user_wins}승 {computer_wins}패 {draws}무")

    elif (user_choice == "가위" and computer_choice == "바위") or\
        (user_choice == "바위" and computer_choice == "보") or\
        (user_choice == "보" and computer_choice == "가위"):
        user_wins += 1
        print(f"승리! 현재 전적 : {user_wins}승 {computer_wins}패 {draws}무")

    elif (user_choice == "가위" and computer_choice == "보") or\
        (user_choice == "바위" and computer_choice == "가위") or\
        (user_choice == "보" and computer_choice == "바위"):
        computer_wins += 1
        print(f"패배! 현재 전적 : {user_wins}승 {computer_wins}패 {draws}무")
    else:
        print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요")
    
    rounds += 1

#결과과
print(f"전적:{user_wins}승 {computer_wins}패 {draws}무")

if user_wins > 2 :
     print("최종 승자: 사용자")
elif computer_wins > 2:
     print("최종 승자: 컴퓨터")