import struct

# 변수 선언: 같은 숫자 '4'이지만 서로 다른 자료형으로 선언됨
num_int = 4          # 정수형 (int)
num_float = 4.0      # 실수형 (float)
num_string = '4'     # 문자열형 (str)

# 정수 2를 정수형 인자(num_int) 비트수로 포맷 (예: 4비트 이진수)
print(format(2, f'0{num_int}b'))     # 출력: 0010

# 실수형 num_float는 format 함수에서 직접 비트수로 사용할 수 없음 → float 비트로 변환 필요
# float → IEEE 754 32비트 변환 후 이진 문자열로 출력
float_bits = struct.unpack('>I', struct.pack('>f', num_float))[0]
print(f'{float_bits:032b}')         # 출력: float 4.0의 32비트 이진 표현

# 문자열형 num_string은 format에서 사용할 수 없음 → int로 변환 후 사용
print(format(int(num_string), '04b'))  # 출력: 0100

# 자료형마다 메모리 상 비트 표현 방식이 다르므로 자료형 확인이 중요함
# 예: int는 이진수 그대로 저장, float은 IEEE 754 부동소수점 형식, str은 유니코드 기반 인코딩

# 비교 연산 예제: 2 == 2.0 + 1.0 은 2 == 3.0 이므로 False → "거짓" 출력
if 2 == 2.0 + 1.0:
    print("참")
else:
    print("거짓")
