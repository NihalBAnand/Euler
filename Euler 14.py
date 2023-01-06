longestChain = []
bestNum = 0
for n in range(13, 999999):
    currentChain = [n]
    temp = n
    while (temp != 1):
        if (temp % 2 == 0):
            temp /= 2
            currentChain.append(temp)
        else:
            temp = (3 * temp) + 1
            currentChain.append(temp)
    if (len(currentChain) > len(longestChain)):
        longestChain = currentChain.copy()
        bestNum = n
print(bestNum)