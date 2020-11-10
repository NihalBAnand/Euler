from math import sqrt
factors = []
pFactors = []
num = 600851475143
div = 1
while div < sqrt(num):
    if (num % div == 0):
        factors.append(div)
    div += 1
div = 1
for i in factors:
    isPrime = True
    while div < sqrt(i):
        if i % div == 0:
            isPrime = False
        div += 1
    if(isPrime):
        pFactors.append(i)
        print(i)
print(max(pFactors))
