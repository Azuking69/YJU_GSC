"""
문자와 숫자가 섞인 문자열에서 숫자만 추출하여 지정된 규칙에 따라 변환하고,
합이 0이 되는 연속된 부분 수열(subarray)을 모두 찾아 출력
"""

#1 사용자로부터 알파벳과 숫자가 섞인 문자열을 입력받는다
user_str = input("문제와 숫자가 섞인 문자열을 입력하세요: \n")
print(f"입력 문자열: {user_str}")

#2 문자열에서 숫자만 추출하여 리스트에 저장
total_list = []

#3 문자열에서 숫자만 추출하여 리스트에 저장
for i in user_str:
    if i.isdigit():
        total_list.append(int(i))

print(f"숫자 추출: {total_list}")

#4 숫자 리스트에 다음 변환 규칙을 적용
conversion_list = []
con_num = 0
for j in total_list:
    if j % 2 == 0:
        con_num = 1
        conversion_list.append(con_num)
    else:
        con_num = -1
        conversion_list.append(con_num)

print(f"변화된 리스트 (+1/-1): {conversion_list}")