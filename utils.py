from math import sqrt
def isPrime(num):
    prime = True
    if num%2 != 0:
        for x in range(2,int(round(num**.5)+1)):
            if num%x ==0:
                prime = False
                break
    else:
        prime = False
    if num ==1:
        prime = False
    if num ==2:
        prime = True
    return prime

def getFactors(num):
    factors = set({})
    div = 1
    while div <= sqrt(num):
        if (num % div == 0):
            factors.add(int(div))
            if (div != 1):
                factors.add(int(num / div))
        div += 1
    return list(factors)
