def get_sum_avg(x:float, y:float, z:float) -> tuple[str, float, float]:
    total = x + y + z
    return "합계, 평균", total, total / 3

result:tuple[str, float, float] = get_sum_avg(1, 2, 3)

print(result[2])