import random

#대문자, 소문자, 숫자를 포함하는 리스트
def generate_password(length):
    #대문자, 소문자, 숫자를 포함한 문자열 정의
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #대문자를 소문자로 변환환
    lowercase_letters = uppercase_letters.lower()
    digits = '0123456789'
    #모든 가능한 문자를 하나의 문자열로 결합
    all_characters = uppercase_letters + lowercase_letters + digits

    #파스워드 초기화
    password = [random.choice(uppercase_letters), random.choice(lowercase_letters), random.choice(digits)]
    
    #모든 가능한 문자를 하나의 문자열로 결합
    all_characters = uppercase_letters + lowercase_letters + digits
    #지정된 길이만큼 랜덤 선택
    password += [random.choice(all_characters) for _ in range(length -3)] #랜덤 문자를 패스워드에 추가
    
# ランダムに並べ替え
    random.shuffle(password)

    #생성된 패스워드 반환
    return ''.join(password)

#characters 리스트에서 랜덤하게 하나의 요소 선택
generated_password = generate_password(8)
print(generated_password)