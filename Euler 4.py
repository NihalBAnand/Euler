maxNum = 100000
num1 = 100
num2 = 100
while num1 <= 999:
    num2 = 100
    while num2 <= 999:
        if (num1*num2 > maxNum) and (str(num1*num2) == str(num1*num2)[::-1]):
            maxNum = num1*num2
        num2 += 1
    num1 += 1
print(maxNum)