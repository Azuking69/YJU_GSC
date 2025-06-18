"""
학생 데이터를 작성
std_score = {'id' : 0, 'name' : 0, 'korean_score' : 0, 'english_score' : 0,\
        'math_score' : 0, 'total' : 0, 'avg' : 0}
"""

std_score = {}        

# menu 작성
menu = """===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료
메뉴 선택(1~5): """

while True:
    # 메뉴 선택
    input_menu = int(input(menu))
    #1. 학생 성적 입력
    if input_menu == 1:
        # 입력 내용         
        user_id = int(input("학번 입력: "))            # 학번 입력
        # 이미 등록된 학번일 경우 저장하지 않고 오류 메시지를 출력
        if user_id in std_score:
            print("이미 등록된 학번입니다.")
            continue

        user_name = input("이름 입력: ")               # 이름 입력
        korean_score = int(input("국어 성적 입력: "))   # 국어 성적
        english_score = int(input("영어 성적 입력: "))  # 영어 성적
        math_score = int(input("수학 성적 입력: "))     # 수학 성적
        
        # total, avg 계산
        total = korean_score + english_score + math_score
        avg = total / 3
        
        # 저장
        std_score[user_id] = {
            'name' : user_name,
            'korean_score' : korean_score,
            'english_score' : english_score,
            'math_score' : math_score,
            'total' : total,
            'avg' : avg
        }
        print("학생 정보가 저장되었습니다.")
        
    #2.학생 성적 출력
    elif input_menu == 2:
        if not std_score:
            print("저장된 학생 정보가 없습니다.")
            continue
        else:
            print("\n학번    이름    국어    영어    수학    합계    평균")
            for i, info in std_score.items():
                print(f"{i}   {info['name']}  {info['korean_score']}     {info['english_score']}      {info['math_score']}      {info['total']}     {info['avg']}")

    #3. 학생 성적 확인
    elif input_menu == 3:
        input_std_num = int(input("조회할 학번 입력: "))
        #존재하지 않는 학번이면 오류 메시지를 출력
        if input_std_num not in std_score:
            print("존재하지 않는 학번입니다.")
            continue
        else:
            info = std_score[input_std_num]
            print(f"""\n[ 학생 정보 ]
학번: {input_std_num}
이름: {info['name']}
국어: {info['korean_score']}
영어: {info['english_score']}
수학: {info['math_score']}
합계: {info['total']}
평균: {info['avg']}
""")

    #4. 학생 성적 삭제
    elif input_menu == 4:
        input_ID = int(input("삭제할 학번 입력: "))
        if input_ID in std_score:
            del std_score[user_id]
            print("학생 정보가 삭제되었습니다.")
        else:
            print("해당 학번의 학생 정보가 없습니다.")

    #5. 종료
    elif input_menu == 5:
        print("프로그램을 종료합니다.")
        break

    #6. 예외처리
    else:
        print("잘못된 입력입니다. 다시 입력하십시오.")