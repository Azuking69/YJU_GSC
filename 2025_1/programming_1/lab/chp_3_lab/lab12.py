#[이 프로그램은 사용자로부터 소득 금액을 입력받아 소득세를 계산]
#[소득세 계산은 다음과 같이 진행됩니다]

#income 패턴으로로 정의
#첫 1만 달러의 소득(income)에는 10%의 세율이 적용됩니다
#1만 달러를 초과하고 2만 달러 이하의 소득에 대해서는 초과 금액에 15%의 세율을 적용하고, 
#첫 1만 달러의 세금인 1천 달러를 더합니다.
#2만 달러를 초과하는 소득에 대해서는 초과 금액에 20%의 세율을 적용하고,
#앞선 구간의세금인 2천 5백 달러를 더합니다
def calculate_tax(income):
    if income <= 10000:
        return income * 0.10
    elif income <= 20000:
        return (income - 10000) * 0.15 + 1000
    else :
        return (income - 20000) * 0.20 + 2500
    
#소득 입력받아        
income = float(input("소득 금액을 입력하세요 :")) #float:소수점, int:정수

#출력
print(f"소득세는 {calculate_tax(income)}달러입니다.")