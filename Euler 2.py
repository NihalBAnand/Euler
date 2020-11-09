sum = 2
part1 = 1
part2 = 2
currentNum = 3
while currentNum <= 4000000:
    if currentNum % 2 == 0:
        sum += currentNum
    part1 = part2
    part2 = currentNum
    currentNum = part1 + part2

print(sum)