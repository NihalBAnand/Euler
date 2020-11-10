from utils import isPrime
primes = [2]
num = 3
while num < 2000000:
    if isPrime(num):
        primes.append(num)
    num += 2
    print(num)
print(sum(primes))