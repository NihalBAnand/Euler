#This program doesn't actually work due to a floating point error. However, it's easy to extrapolate from the answer that it provides what the correct answer is.

from fractions import Fraction
from math import prod

answers = set({})
for numerator in range(10, 100):
    for denominator in range(10, 100):
        if denominator < numerator:
            continue
        
        if (numerator % 10 == 0 and denominator % 10 == 0) or numerator == denominator:
            continue

        strNum = str(numerator)
        strDen = str(denominator)

        strNum = "".join(sorted(strNum))
        strDen = "".join(sorted(strDen))
        sameNumber = ""
        if strNum[0] != strDen[0] and strNum[1] != strDen[1]:
            continue
        
        if strNum[0] == strDen[0]:
            sameNumber = strNum[0]
        elif strNum[1] == strDen[1]:
            sameNumber = strDen[1]
        
        
        strNum = str(numerator)
        strDen = str(denominator)
        try:
            testFraction = int(strNum.replace(sameNumber, "", 1)) / int(strDen.replace(sameNumber, "", 1))
        except ZeroDivisionError:
            continue
        if testFraction == numerator / denominator:
            answers.add(numerator / denominator)

print(Fraction(prod(answers)))
