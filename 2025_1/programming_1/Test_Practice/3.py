"""
딕셔너리를 활용하여 학생의 성적을 입력, 출력, 조회, 삭제하는 메뉴 기반 프로그램을 작성.
각 학생은 학번을 기준으로 저장되며, 이름, 국어, 영어, 수학 성적의 합계와
평균도 함께 저장.
"""
std_score = {}
# 메뉴 작성
menu = """===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료
메뉴 선택(1~5): """

# 메뉴를 반복적으로 출력
while True:
    # 메뉴 출력
    input_menu = int(input(menu))

    #1. 학생 성적 입력
    if input_menu == 1:
        student_num = int(input("학번을 입력: "))        # 학번 입력
        # 이미 등록된 학번일 경우 저장하지 않고 오류 메시지를 출력
        if student_num in std_score:
            print("이미 등록된 학번입니다.\n")
            continue

        student_name = input("이름을 입력: ")            # 이름 입력
        korean_score = int(input("국어 성적을 입력: ")) # 국어 성적
        english_score = int(input("영어 성적을 입력: "))       # 영어 성적
        math_score = int(input("수학 성적을 입력: "))          # 수학 성적
        
        # total, avg 계산
        total = korean_score + english_score + math_score
        avg = total / 3

        # 저장
        std_score[student_num] = {
            '이름' : student_name,
            '국어' : korean_score,
            '영어' : english_score,
            '수학' : math_score,
            '합계' : total,
            '평균' : avg
        }
        print("성적이 저장되었습니다.\n")

    #2. 학생 성적 출력
    elif input_menu == 2:
        # 학번 확인
        if not std_score:
            print("저장된 학생 정보가 없습니다.\n")
        else:
            # 출력
            print("\n[ 전체 학생 성적 ]")
            print("학번   이름    국어   영어   수학   합계   평균")
            # 학번마다 가져오기
            for i, info in std_score.items():
                print(f"{i}  {info['이름']}  {info['국어']}    {info['영어']}     {info['수학']}    {info['합계']}    {info['평균']}")

    #3. 학생 성적 확인
    elif input_menu == 3:
        input_ID = int(input("조회할 학번 입력: "))
        # 존재하지 않는 학번이면 오류 메시지를 출력
        if input_ID not in std_score:
            print("해당 학번의 학생 정보가 없습니다.\n")
        # 특정 학번을 입력받아 해당 학생의 성적 정보를 출력
        else:
            info = std_score[input_ID]
            print(f"""\n[ 학생 정보 ]
학번: {input_ID}
이름: {info['이름']}
국어: {info['국어']}
영어: {info['영어']}
수학: {info['수학']}
합계: {info['합계']}
평균: {info['평균']}\n""")

    #4. 학생 성적 삭제
    elif input_menu == 4:
        input_ID = int(input("삭제할 학번 입력: "))
        #존재하지 않는 학번이면 오류 메시지를 출력
        if input_ID not in std_score:
            print("해당 학번의 학생 정보가 없습니다.\n")
        #특정 학번을 입력받아 해당 학생의 정보를 삭제
        else:
            del std_score[input_ID]
            print("학생 정보가 삭제되었습니다.\n")

    #5. 종료
    elif input_menu == 5:
        print("프로그램을 종료합니다.")
        break

    #6. 예외 처리
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")