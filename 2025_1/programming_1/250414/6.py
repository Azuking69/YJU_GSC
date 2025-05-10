#점수를 임력 받아
#입력 점수가 0보다 작으면 
#"입력 값 오류" 출력 후
score = int(input("점수 입력: "))

if score < 0:
    print("입력 값 오류")
#입력 값이 0 이상일 경우 합격 여부(可否) 판단
else:
    pass
    #입력 값이 0 이상일 경우 합격 여부 판단

    #if-else: 점수가 80점 이상이면 "합격"
    #아니면 "불합격"
    if score >= 80:
        print("합격")
    else:
        print("불합격")
    
    #if-elif-else:
    #점수에 따라 등급 부여(90:A, 80:B, 70:C, 그외:D)
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"

    #층첨 if: A등급이면서 등시에 95점 이상이면
    #"우수상" 출력
    if grade == "A":
        if score >= 95:
            print("우수상")
    #추가 조건: 점수가 100이면 "면점 축하!" 출력
    if score == 100:
        print("면점 축하!")
