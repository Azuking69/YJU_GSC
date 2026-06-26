"""
딕셔너리를 이용하여 학생 성적 관리 프로그램을 작성하라
"""
student_list = {}

input_data = 0
std_avg = 0.0

while True:
    #1 menu작성
    menu = f"""====================
    1. 학생 성적 입력
    2. 학생 목록 출력
    3. 프로그램 종류

    현 입력데이터 갯수: {input_data}
    전체 학생 평균 값 : {std_avg:.2f}
    ====================
    """

    #2 입력
    input_menu = int(input(menu))

    #3 학생 성적 입력
    if input_menu == 1:
        input_num = int(input("학번을 입력하세요: "))
        input_name = int(input("이름을 입력하세요: "))
        input_nat_lang = int(input("국어 성적을 입력하세요: "))
        input_english = int(input("영어 성적을 입력하세요: "))
        input_math = int(input("수학 성적을 입력하세요: "))

        #4 계산
        total = input_nat_lang + input_english + input_math
        total_avg = total / 3
        
        #5 리스트화
        student_list[input_num] = {
            'id' : input_num,
            'name' : input_name,
            'kor' : input_nat_lang,
            'eng' : input_english,
            'math' : input_math,
            'avg' : total_avg
        }
        #6 리스트 내용수/평균 계산
        input_data += 1
        std_avg = round(sum(std['avg'] for std in student_list.values()) / input_data)

    # 학생 목록 출력
    elif input_menu == 2:
        for std in student_list.value():
            print(f"id: {std('id')} name: {std('name')} kor: {std('kor')} eng: {std('eng')} math: {stu['math']} sum: {stu['sum']} avg: {stu['avg']}")

    else:
        print("프로그램 종료")
        break