curNum = 1
primes = []
while len(primes) < 10001:
	isPrime = 1
	for i in range(2, curNum):
		if curNum % i == 0:
			isPrime = 0
	if isPrime:
		primes.append(curNum)
	curNum += 1
	
print('Answer: ' + primes[10000])