from math import pow
start = 4150
anses = []
while start < 999999:
	tem = str(start)
	t = 0
	for i in tem: t += pow(int(i), 5)
	if t == start: anses.append(start)
	start += 1
print(sum(anses))
