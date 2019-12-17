sqrsum = 0
sumsqr = 0
sum2 = 0

i = 1
while i < 101:
	sumsqr += i**2
	i += 1
i = 1
while i < 101:
	sum2 += i
	i += 1
sqrsum = sum2**2
ans = sqrsum - sumsqr
print(str(ans))