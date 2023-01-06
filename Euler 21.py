from utils import getFactors
amicables = 0
for a in range(1, 10000):
    b = sum(getFactors(a))
    if (a != b and sum(getFactors(b)) == a):
        amicables += a
        print(a, b)
        print(str((a / 10000) * 100) + "%")
print(amicables)