word = input("단어를 입력하세요: ")

count = 0

for _ in word:
    count += 1

print(f"입력 단어 {word}의길이는 {count}")