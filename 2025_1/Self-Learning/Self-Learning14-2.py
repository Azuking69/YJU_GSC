#사용자 입력 받기
numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요:")

#문자열을 숫자 리스트로 변환
numbers = numbers_str.split(',')

#각 숫자를 정수로 변환
numbers = list(map(int,numbers))

#모든 숫자의 합
total = sum(numbers)

#총합이 100을 초과하면 해당 순간의 입력 값들과 총합을 출력하고 프로그램을 종료
if total > 100 :
    print(f"총합이 100을 초과하였습니다."
        f"현재까지의 입력값들: {numbers}"
        f"현재까지의 총합: {total}")
else :
    print(f"총합이 100을 초과하지 않았습니다"
        f"입력된 모든 숫자들:{numbers}"
        f"최종 총합:{total}")