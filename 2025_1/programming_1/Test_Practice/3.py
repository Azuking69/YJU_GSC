"""
딕셔너리를 활용하여 학생의 성적을 입력, 출력, 조회, 삭제하는 메뉴 기반 프로그램을 작성.
각 학생은 학번을 기준으로 저장되며, 이름, 국어, 영어, 수학 성적의 합계와
평균도 함께 저장.
"""

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
    input_menu = int(input(menu))

    #1. 학생 성적 입력
    if input_menu == 1:
        student_num = int(input("학번을 입력: "))
        student_name = input("이름을 입력: ")
        national_lang = int(input("국어 성적을 입력: "))
        english = int(input("영어 성적을 입력: "))
        math = int(input("수학 성적을 입력: "))
        