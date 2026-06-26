import random
#1 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장
while True:
    user_input1 = input("첫 번째 단어를 입력하세요").strip()
    user_input2 = input("두 번째 단어를 입력하세요").strip()
    user_input3 = input("세 번째 단어를 입력하세요").strip()

#2 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구
    if (len(user_input1) < 4 or len(user_input2) < 4 or len(user_input3) < 4) or\
        (21 < len(user_input1) or 21 < len(user_input2) or 21 < len(user_input3)):
        print("단어의 글자 범위 5 이상, 20 이하로 입력하세요.")
        continue
    break

words_list = [user_input1 , user_input2 , user_input3]

#3 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
computer_select = random.choice(words_list)
print(f"단어 선택 완료 개임을 시작합니다. 선택된 단어:{computer_select}")

#4 Blind 처리
def blind_word(word):
    word_list = list(word)
    blind_count = (len(word) + 1) // 2 #단어 길이의 50%를 Blind 처리
    blind_indices = random.sample(range(len(word)), blind_count)
    blinded_word = ["_" if i in blind_indices else word_list[i] for i in range(len(word))]
    return blinded_word

#5 첫 번째 blind 출력
blinded_word = blind_word(computer_select)
count = 0

while "_" in blinded_word:
    count += 1
    print(f"\n{count}번째 시도, 아래 단어를 구성하는 알파뱃 한 개 입력하세요.")
    print("현재 단어 상태 : ", "".join(blinded_word))
    input_character = input("입력:").strip().lower()
   
#6 입력한 글자를 판단
    if input_character in computer_select:
        found = False
        for i in range(len(computer_select)):
            if computer_select[i] == input_character and blinded_word[i] == "_":
                blinded_word[i] = input_character
                found = True
        print(f"입력한 알파벳 단어 내 포함: {computer_select.count(input_character)}글자")

    else :
        print("단어 내 포함되지 않은 알파벳입니다.")    

# 결과
print(f"Clear - 선택된 단어 : {computer_select}, 총 시도 횟수 : {count}")