sum = 0
for i in range(1, 1002, 2):
    sum += 4*(i**2) - 6*i + 6
sum -= 3
print(sum)