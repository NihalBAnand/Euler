from math import sqrt
for a in range(1, 1000):
    for b in range(2, 1000):
        if ((sqrt(a**2 + b**2)).is_integer()):
            c = sqrt(a**2 + b**2)
            if (a + b + c) == 1000:
                print(a * b * c)
                break