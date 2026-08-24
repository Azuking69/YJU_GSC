# 구조적언어 구성요소
from unittest import result


bar = 2
foo = 3.0

def even_ood(a, b):
  result = bar + foo #변수와 연산자를 이용 -> 식

  if result % 2 == 0:
    print("짝수")
  else:
    print("홀수")