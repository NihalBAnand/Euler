from utils import getFactors

sumNonAbundantSums = 0

abundants = []
for i in range(28123):
    if (sum(getFactors(i)) > i):
        abundants.append(i)
print(len(abundants))

abundantSums = set({})
for i in abundants:
    for j in abundants:
        abundantSums.add(i + j)
print(len(abundantSums))


for i in range(28123):
    if (not i in abundantSums):
        sumNonAbundantSums += i
print(sumNonAbundantSums)




