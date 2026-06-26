# 정수 3개 입력 
# input_value1 = int(nput("첫 번째 값을 입력하세요: "))
input_value1 = input("첫 번째 값을 입력하세요: ")
input_value2 = input("두 번째 값을 입력하세요: ")
input_value3 = input("세 번째 값을 입력하세요: ")

print("첫 번째 값: ", input_value1, " type: ", type(input_value1))
print("두 번째 값: ", input_value2, " type: ", type(input_value2))
print("세 번째 값: ", input_value3, " type: ", type(input_value3))

input_value1 = int(input_value1)
input_value2 = int(input_value2)
input_value3 = int(input_value3)

print(f"첫 번째 값: {type(input_value1)}, 두 번째 값:{type(input_value2)}\
    , 세 번째 값: {type(input_value3)}")

# 평균 구하기 : avg = (input_value1 + input_value2 + input_value3) / 3
avg = (input_value1 + input_value2 + input_value3) / 3

# 출력: 값과 자료형
print(f"평균: {avg}, 자료형: {type(avg)}")