# SORTING FILE CODE
# names = open("euler22_names.txt").read()
# names = names.split(",")
# names = [name.replace('"', "") for name in names]
# names.sort()
# sortedNames = open("euler22_names_sorted.txt", "w")
# [str(sortedNames.write(name + " ")) for name in names]

#CALCULATING SCORES CODE
names = open("euler22_names_sorted.txt").read()
names = names.split(" ")

scores = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

sumScores = 0
for name in names:
    nameScore = sum([scores[letter] for letter in name])
    nameScore *= names.index(name) + 1
    sumScores += nameScore
print(sumScores)