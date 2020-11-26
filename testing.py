from utils import isPrime
primes = [2] 
num = 3
while num < 1000:
    if isPrime(num):
        primes.append(num)
    num += 2
print(sum(primes))