#사용자로부터 "left", "right", "up", "down" 중 하나의 단어를 입력받습니다.
x = input("방향을 입력하세요(left, right, up, down)")

#입력받은 문자열에 따라 "왼쪽으로 이동합니다", "오른쪽으로 이동합니다", "위로이동합니다", 
#"아래로 이동합니다"를 출력하는 프로그램을 작성
if x == 'left':
    print("왼쪽으로 이동합니다.")
elif x == 'right':
    print("오른쪽으로 이동합니다.")
elif x == 'up':
    print("위로 이동합니다.")
elif x == 'down':
    print("아래로 이동합니다.")
else :
    print("알 수 없는 명령어입니다.")