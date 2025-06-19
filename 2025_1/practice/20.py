"""
딕셔너리를 활용하여 상품의 정보를 입력, 출력, 조회, 삭제할 수 있는 
메뉴 기반 프로그램을 작성.
각 상품은 상품코드를 기준으로 저장되며, 상품명, 수량, 단가, 총액(수량×단가) 정보를 저장.
"""
# 메뉴 작성
menu = """
===== 상품 재고 관리 프로그램 ======
1. 상품 등록
2. 전체 상품 목록 출력
3. 특정 상품 정보 조회
4. 상품 삭제
5. 종료
메뉴 선택: """

product_list = {}

while True:
    # 입력을 받는다
    input_menu = int(input(menu))

    # 상품 등록
    if input_menu == 1:
        product_code = int(input("상품코드 입력: "))
        # 이미 등록된 상품코드일 경우 저장하지 않고 오류 메시지 출력
        if product_code in product_list:
            print("이미 등록된 상품코드입니다.")
        else:
            product_name = input("상품명 입력: ")
            product_count = int(input("수량 입력: "))
            product_price = int(input("단가 입력: "))

            # 총액 계산
            total = product_count * product_price

            # 저장
            product_list[product_code] = {
                '상품명' : product_name,
                '수량' : product_count,
                '단가' : product_price,
                '총액' : total
            }

    # 전체 상품 목록 출력
    elif input_menu == 2:
        if not product_list:
            print("상품 정보가 없습니다.")

        else:
            print("[ 전체 상품 목록 ]")
            print("상품코드\t상품명\t수량\t단가\t총액")
            for i, info in product_list.items():
                print(f"{i}\t{info['상품명']}\t{info['수량']}\t{info['단가']}\t{info['총액']:.2f}")

    # 특정 상품 조회
    elif input_menu == 3:
        input_ID = int(input("조회할 상품코드 입력: "))
        if input_ID not in product_list:
            print("해당 상품 정보가 없습니다.")
        else:
            info = product_list[input_ID]
            print(f"""[ 상품 정보 ]
상품코드: {input_ID}
상품명: {info['상품명']}
수량: {info['수량']}
단가: {info['단가']}
총액: {info['총액']}""")

    # 상품 삭제
    elif input_menu == 4:
        input_ID = int(input("삭제할 상품코드 입력: "))
        if input_ID not in product_list:
            print("해당 상품 정보가 없습니다.")
        else:
            del product_list[input_ID]
            print("상품 정보가 삭제되었습니다.")

    # 종료
    elif input_menu == 5:
        print("프로그램을 종료합니다.")
        break

    # 예외 처리
    else:
        print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")