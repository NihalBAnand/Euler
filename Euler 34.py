from math import factorial
start = 3
anses = []
while start < 999999:
	tem = str(start)
	t = 0
	for i in tem: 
		t += factorial(int(i))
	if t == start: 
		anses.append(start)
	start += 1
print(sum(anses))

