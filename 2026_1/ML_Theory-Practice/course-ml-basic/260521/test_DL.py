from turtle import pos

import numpy as np

# bar = np.arange(1, 10).reshape(3, 3)
bar = np.arange(16).reshape(4, 4)
print(bar)

bar = bar + 1
print(bar)
print(bar % 2 == 0)

print(bar[bar % 2 == 0])
print(np.where(bar % 2 == 0, bar, 0))

pos = np.where(bar % 2 == 0, bar, 0)
print(pos[1:3, 2:4])
