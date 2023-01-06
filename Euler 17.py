ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tenThruNineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

totalLetters = sum([len(item) for item in ones]) + sum([len(item) for item in tenThruNineteen])

for i in range(20, 1001):
    temp = str(i)
    j = i
    built = ""
    if (i == 1000):
        built = "onethousand"
        totalLetters += len(built)
        continue
    
    if (i > 100 and i % 100 != 0):
        built += ones[int(temp[0]) - 1] + "hundredand"
    elif (i % 100 == 0):
        built += ones[int(temp[0]) - 1] + "hundred"
        totalLetters += len(built)
        continue
    else:
        built += tens[int(temp[0]) - 2]
        j %= 10
        if (j == 0):
            totalLetters += len(built)
            continue
        temp = str(j)
        built += ones[int(temp[0]) - 1]
        totalLetters += len(built)
        continue
    
    j %= 100
    temp = str(j)
    if (j >= 10 and j <= 19):
        built += tenThruNineteen[int(temp[1])]
    elif (j < 10):
        built += ones[int(temp[0]) - 1]
    else:
        built += tens[int(temp[0]) - 2]
        j %= 10
        if (j == 0):
            totalLetters += len(built)
            continue
        temp = str(j)
        built += ones[int(temp[0]) - 1]

    totalLetters += len(built)
print(totalLetters)