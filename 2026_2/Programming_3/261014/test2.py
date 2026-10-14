from typing import NamedTuple

class ResulitAvgSum(NamedTuple):
    title: str
    total: float
    avg: float

# 조건: 입력 값은 숫자
def get_sum_avg(x:float, y:float, z:float) -> ResulitAvgSum:
    total = x + y + z
    return ResulitAvgSum("합계, 평균", total, total / 3)

result:ResulitAvgSum = get_sum_avg(1, 2, 3)

print(result.avg)