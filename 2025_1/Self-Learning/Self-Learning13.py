#첫 번째 입력은 검사할 전체 문자열이며
msg1 = input("문자열 입력:")

#두 번째 입력은 출현 빈도를 확인할 단어
msg2 = input("단어 입력:")

count = 0
word = ""

# 3. 文字列を1文字ずつ走査
for char in msg1:
    if char != " ":  # 空白でない場合、単語を構築
        word += char
    else:
        if word == msg2:  # 空白が来たら、前の単語をチェック
            count += 1
        word = ""  # 単語をリセット

# 4. 最後の単語もチェック（ループが終わった後に単語が残っている場合）
if word == msg2:
    count += 1

# 5. 結果を表示
print(count)