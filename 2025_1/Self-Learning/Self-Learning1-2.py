"""
사용자가 입력한 세 개의 수를 변의 길이로 하는 삼각형이 형성될
수 있는지, 그리고 가능하다면 어떤 유형의 삼각형인지 판별

기준
① 만약 세 변의 길이가 모두 같다면, '정삼각형'입니다.
② 만약 세 변 중 두 변의 길이가 같다면, '이등변삼각형'입니다.
③ 만약 세 변의 길이가 모두 다르다면, '부등변삼각형'입니다.
④ 만약 어느 두 변의 길이 합이 나머지 한 변의 길이보다 작거나 같다면, 삼각형을 형성
"""

#1 정의
def triangle(input1, input2, input3):
    if input1 + input2 < input3 or input1 + input3 < input2 or input2 + input3 < input1:
        msg = "삼각형을 만들 수 없습니다.\n삼각형을 만들기 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다."
        return msg
    elif input1 == input2 == input3:
        msg = "'정삼각형'"
        return msg
    elif input1 == input2 or input1 == input3 or input2 == input3:
        msg = "'이등변삼각형'"
        return msg
    else:
        msg = "'부등변삼각형'"
        return msg
    
#2 입력력   
input1 = int(input("첫 번째 변의 길이를 입력하세요:"))
input2 = int(input("두 번째 변의 길이를 입력하세요:"))
input3 = int(input("세 번째 변의 길이를 입력하세요:"))

#3 출력
msg = triangle(input1, input2, input3)
if "삼각형을 만들 수 없습니다" in msg:
    print(f"입력하신 변의 길이로는 {msg}")
else:
    print(f"입력하신 변의 길이로는 {msg}을 만들 수 있습니다 .")
    