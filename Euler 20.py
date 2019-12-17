from math import factorial

big = factorial(100)
l = str(big)
add = []
for i in l:
	add.append(int(i))
x = sum(add)
print(str(x))