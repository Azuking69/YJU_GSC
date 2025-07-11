#키보드로부터 두 개 정수를 입력 받아 저장 후
input_value1 = int(input("첫 번째 입력 값: \t"))
input_value2 = int(input("두 번째 입력 값: \t"))

#아래 매뉴를 출력하세요
menu = """-----------
1.더하기
2.빼기
3.곱하기
4.나누기
----------"""
print(menu)

#test-1
#print(f"{input_value1} + {input_value2} = {input_value1 + input_value2}")

#매뉴 출력 후 다시 키보드로부터 매뉴 선택값을 입력 받고,
sel_menu = int(input("메뉴를 선택하세요!\t"))

#선택한 연산자에 따라 이전 입력 받은 두 수의 연산값을 출력하세요.
    result = 0
if sel_menu == 1:
    result = input_value1 + input_value2

elif sel_menu == 2:
    result = input_value1 - input_value2

elif sel_menu == 3:
    result = input_value1 * input_value2

elif sel_menu == 4:
    presult = input_value1 / input_value2

else :
    result = "잘못된 입력 입니다."

#결과
print(result)


