import numpy as np
x = 9
a = 1
b = x
g = np.random.uniform(1, x)
e = b - a
n = 0
while e > 0.01:
    if g**2 > x:
        b = g
    elif g**2 < x:
        a = g
    e = b - a
    g = (a + b) / 2
    n += 1
print((a+b)/2)
print(n)