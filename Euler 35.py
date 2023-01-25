from utils import isPrime
answers = []
for num in range(1, 1000001):
    if isPrime(num):
        strNum = str(num)
        flag = False
        for i in range(len(strNum)):
            strNum, temp = strNum[:-1], strNum[-1]
            strNum = temp + strNum

            if not isPrime(int(strNum)):
                flag = True
                break
        
        if not flag:
            answers.append(num)

print(len(answers))