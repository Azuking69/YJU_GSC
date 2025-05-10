#입력한 문자
myStrings = "hello hyundai hoho"

#리스트화
list_myStrings = list(myStrings)

#h 확인인
h_character = [character for character in list_myStrings if character == "h"]

#수량 확인인
count = len(h_character) 

#출력
print("문자열 내 h갯수 :", count)