"""
For 문을 사용하여 아래 문자열 내 단어 개수를 출력
"""
# 문자열
myString = "It is a great weather with you"

# count 정의
count = 0

# for문으로 검사
for char in myString:
    #" "가 있으면 앞에 단어를 1개로 정의
    if char == " ":
        count += 1

# 전체 검사가 끝나면 마지막 단어를 더하고 출력
print(f"문자열 단어 갯수: {count + 1}")