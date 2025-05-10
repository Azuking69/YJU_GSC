#1 문자열 검색을 위한 사전 입력 문장
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

#2 whileで終了までのループと定義
while True:
    user_input = input("검색할 문자열을 입력하세요: ")

    if user_input in sentence:
        #몇 개 있는지 확인
        sentence_count = sentence.count(user_input)

        #어디에 있는지 확인
        positions = []  # list화
        index = sentence.find(user_input) #sentence에서 추출
        while index != -1:
            positions.append(index)
            index = sentence.find(user_input, index + 1) #終わったところから続けてくれる

        print(f"검색된 문자열의 개수: {sentence_count}")
        print(f"검색된 문자열의 위치: {positions}")

        

        words = sentence.split() #split() は空白文字（スペース・改行・タブ）で単語を自動的に分けてくれる
        print(f"단어 개수:{len(words)}")

        print(f"전체 문자 수:{len(sentence)}")

        lines = sentence.splitlines()
        line_count = len(lines)
        print(f"줄 수:{line_count}")
        break 

    else:
        print("해당 문자열이 없습니다. 다시 입력하세요.")
   

#개행 문자가 포함된 여러 줄 문자열 출력

#""" """ 구문은 여러 줄 문자열(Multiline string)을 정의하는데 사용된다
#이를 활용하여 개행(改行) 문자가 포함된 여러 줄 문자열을 효율적으로 작성할 수 있다