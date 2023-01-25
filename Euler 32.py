answers = set({})
for a in range(0, 9999):
    for b in range(0, 999):
        c = a * b
        if (len(str(a)) + len(str(b)) + len(str(c)) == 9):
            if "".join(sorted(str(a) + str(b) + str(c))) == "123456789":
                answers.add(c)

print(sum(answers))