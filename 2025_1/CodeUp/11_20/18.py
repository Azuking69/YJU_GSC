"""
24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
"""
#1 24시간 시:분 형식으로 시간이 입력
input_hour, input_time = input("24시간 시:분 형식으로 시간이 입력: ").split(':')

#2 그대로 출력
print(input_hour, input_time, sep=':')