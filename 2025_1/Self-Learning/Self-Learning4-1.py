"""
사용자는 이 시뮬레이터를 통해 초기 자본금으로 주식을 구매
이후 주식 가격이 변동한 후에 주식을 판매하여 얻는 이익이나 발생하는 손실을 계산
"""

#1 정보를 입력
user_capital = int(input("초기 자본금을 입력하세요: "))
stock_price = int(input("주식 가격을 입력하세요: "))
stock_count = int(input("구매할 주식 수를 입력하세요: "))
stock_sale_price = int(input("판매할 때의 주식 가격을 입력하세요: "))

#2 정의
def stock_accouting():
    #주식 구매 비용 계산
    stock_expense = stock_price * stock_count
    #남은 자본금 계산
    user_total_capital = user_capital - stock_expense
    #판매 예상 이익 계산
    user_profit = stock_sale_price * stock_count
    #
    print(f"구매 후 남은 자본금: {user_total_capital:.2f}")

    #이익 판단
    #이익이 발생
    if stock_expense - user_profit > 0:
        colect = "이익"
    else:
        colect = "손실"
    
    print(f"예상 이익: {user_profit:.2f}")
    print(f"예산되는 {colect}입니다.")

stock_accouting()