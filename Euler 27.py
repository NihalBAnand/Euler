from utils import isPrime

maxPrimes = 0
bestA = 0
bestB = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        currentPrimes = 0
        n = 0
        while isPrime(abs(int(n**2) + a*n + b)):
            n += 1
            currentPrimes += 1
        if currentPrimes > maxPrimes:
            maxPrimes = currentPrimes
            bestA = a
            bestB = b

print(bestA * bestB) 