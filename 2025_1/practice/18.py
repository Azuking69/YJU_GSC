"""
공백으로 구분된 문자열에서 특정 글자 수 이상인 단어를 찾아서 
개수와 위치(인덱스)를 출력하는 프로그램을 작성
"""
#1 미리 정의된 문자열 
text = "banana apple cat programming kiwi python language"
#2 사용자에게 기준 글자 수(정수)를 입력받는다
input_num = int(input("기준 단어 길이를 입력하세요: "))

#3 각 단어의 길이를 확인
word = ""
word_list = []

for char in text:
    if char != " ":
        word += char

    elif word != "":
        word_list.append(word)
        word = ""

if word:
    word_list.append(word)

print(word_list)