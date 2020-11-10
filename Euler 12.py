from utils import getFactors
num = 1
bigNum = 0
biggestFactors = []
while len(biggestFactors) <= 500:
    tempSum = 0
    for i in range (num):
        tempSum += i
    currentFactors = getFactors(tempSum)
    if len(currentFactors) > len(biggestFactors):
        biggestFactors = currentFactors
        bigNum = tempSum
        print(bigNum)
    num += 1
print(bigNum)    