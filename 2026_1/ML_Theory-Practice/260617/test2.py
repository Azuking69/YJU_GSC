import numpy as np

bar = np.arange(12).reshape(3, 4)

print(f"bar: {bar}\n")

bar_min_max =  (bar - bar.min(0)) / (bar.max(0) - bar.min(0))

bar_std = (bar - bar.mean(0)) / bar.std(0)
print(bar_min_max)
print(bar_std)