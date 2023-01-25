from utils import isPrime

longestOrder = 0
bestNum = 0
for i in range(6, 1001):
    if (not isPrime(i)):
        continue
    remainder = 0
    currentOrder = 0
    while remainder != 1:
        currentOrder += 1
        remainder = 10**currentOrder % i 
    if (currentOrder > longestOrder):
        longestOrder = currentOrder
        bestNum = i
print(longestOrder, bestNum)
#https://www.quora.com/Is-there-a-known-formula-for-how-long-repeating-decimal-sequences-are-based-on-the-numerator-and-denominator