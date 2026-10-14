def get_sum_avg(x:float, y:float, z:float) -> tuple[float, float]:
    total = x + y + z
    return total, total / 3

print(type(get_sum_avg(1, 2, 3)))