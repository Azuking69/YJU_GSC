"""
딕셔너리를 활용하여 학생의 성적을 입력, 출력, 조회, 삭제하는 메뉴 기반 프로그램을 작성.
각 학생은 학번을 기준으로 저장되며, 이름, 국어, 영어, 수학 성적의 합계와
평균도 함께 저장.
"""
# 성적 저장 dictionary 작성
std_score = {}

# menu 작성
menu = """
===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료
메뉴 성택: """

#메뉴를 반복적으로 출력
while True:
    input_menu = input(menu)

    #1. 학생 성적 입력
    if input_menu == "1":
        # 학번(정수), 이름(문자열), 국어/영어/수학 성적(정수)을 입력받는다
        std_ID = int(input("학번 입력: "))
        # 이미 등록된 학번일 경우 저장하지 않고 오류 메시지를 출력한다
        if std_ID in std_score:
            print("이미 등록된 학번입니다.")

        else:
            std_name = input("이름 입력: ")
            korean_score = int(input("국어 성적 입력: "))
            english_score = int(input("국어 성적 입력: "))
            math_score = int(input("국어 성적 입력: "))

            # 입력받은 성적의 합계(정수)와 평균(실수, 소수점 2자리)를 계산
            total = korean_score + english_score + math_score
            avg = total / 3

            # 저장한다
            std_score[std_ID] = {
                '이름' : std_name,
                '국어' : korean_score,
                '영어' : english_score,
                '수학' : math_score,
                '합계' : total,
                '평균' : avg
            }

            # 저장 완료 출력
            print("성적이 저장되었습니다.") 

    #2. 학생 성적 출력
    elif input_menu == "2":
        # 데이터 없을 때
        if not std_score:
            print("저장된 학생 정보가 없습니다.")

        # 저장된 전체 학생의 성적 정보를 출력한다
        else:
            print("[ 전체 학생 정보 ]")
            # 출력 항목: 학번, 이름, 국어, 영어, 수학, 합계, 평균
            print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
            for i, info in std_score.items():
                print(f"{i}\t{info['이름']}\t{info['국어']}\t{info['영어']}\t{info['수학']}\t{info['합계']}\t{info['평균']}")

    #3. 학생 성적 확인
    elif input_menu == "3":
        # 특정 학번을 입력받는다
        input_ID = int(input("조회할 학번 입력: "))
        # 존재하지 않는 학번이면 오류 메시지를 출력
        if input_ID not in std_score:
            print("해당 학번의 학생 정보가 없습니다.")

        # 해당 학생의 성적 정보를 출력
        else:
            info = std_score[input_ID]
            print(f"""[ 학생 정보 ]
                학번: {input_ID}
                이름: {info['이름']}
                국어: {info['국어']}
                영어: {info['영어']}
                수학: {info['수학']}
                합계: {info['합계']}
                평균: {info['평균']}""")

    #4. 학생 성적 삭제
    elif input_menu == "4":
        # 특정 학번을 입력받는다
        input_ID = int(input("삭제할 학번 입력: "))
        # 존재하지 않는 학번이면 오류 메시지를 출력
        if input_ID not in std_score:
            print("해당 학번의 학생 정보가 없습니다.")

        # 해당 학생의 정보를 삭제한다
        else:
            del std_score[input_ID]
            # 삭제 완료 출력
            print("학생 정보가 삭제되었습니다.")

    #5. 종료
    elif input_menu == "5":
        print("프로그램을 종료합니다.")
        break

    # 예외 처리
    else:
        print("잘못된 입력입니다. 1~5 사이의 숫자를 선택하세요.")