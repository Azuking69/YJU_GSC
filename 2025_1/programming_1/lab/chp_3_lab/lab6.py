#사용자로부터 나이를 입력받습니다. (정수형으로 가정)
age = int(input("나이를 입력하세요 :"))
#입력된 나이에 따라 사용자를 "청소년(Teenager)", "성인(Adult)", "노년(Senior)" 중 하나로분류합니다. 
#13세에서 19세 사이는 "Teenager"
if 13 < age < 19:
    print("You are in the 'Teenager' age group.")
#20세에서 64세 사이는 "Adult"
elif 20 < age < 64:
      print("You are in the 'Adult' age group.")
#65세 이상은 "Senior"
elif 65 < age:
    print("You are in the 'Senior' age group.")
#해당하는 나이대의 영어 단어를 화면에 출력

#범위에 맞지 않는 입력값에 대해서는 "Unknown age group"이라고 출력