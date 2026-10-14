from typing import NamedTuple

class ResultAvgSum(NamedTuple):
    title: str
    total: float
    avg: float

# 조건: 입력 값은 숫자
def get_sum_avg(x:float, y:float, z:float) -> ResultAvgSum:
    total = x + y + z
    return ResultAvgSum("합계, 평균", total, total / 3)

result:ResultAvgSum = get_sum_avg(1, 2, 3)

print(result.avg)
print(ResultAvgSum.mro())