from math import pow
anses = []
tsu = 0
t = 0
ts = 0
for a in range(0, 100):
	for b in range(0, 100):
		t = a**b
		ts = str(t)
		tsu = 0
		
		for i in ts:
			tsu += int(i)
		anses.append(tsu)

	print(a)

print(max(anses))