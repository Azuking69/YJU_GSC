myString = "It is a great weather with you"

words = myString.split()

count = 0
for word in words:
    count += 1

print("문자열 단어 갯수 : ", count)