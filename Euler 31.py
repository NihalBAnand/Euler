#Euler 31
solutions = set({})
for twoPounds in range(0, 2):
    if (200 * twoPounds == 200):
        solutions.add((twoPounds, 0, 0, 0, 0, 0, 0, 0))
        continue
    for onePound in range(0, 3):
        if (200 * twoPounds + 100 * onePound == 200):
            solutions.add((twoPounds, onePound, 0, 0, 0, 0, 0, 0))
            continue
        for fiftyP in range(0, 5):
            if (200 * twoPounds + 100 * onePound + 50 * fiftyP == 200):
                solutions.add((twoPounds, onePound, fiftyP, 0, 0, 0, 0, 0))
                continue
            for twentyP in range(0, 11):
                if (200 * twoPounds + 100 * onePound + 50 * fiftyP + 20 * twentyP == 200):
                    solutions.add((twoPounds, onePound, fiftyP, twentyP, 0, 0, 0, 0))
                    continue
                for tenP in range(0, 21):
                    if (200 * twoPounds + 100 * onePound + 50 * fiftyP + 20 * twentyP + 10 * tenP == 200):
                        solutions.add((twoPounds, onePound, fiftyP, twentyP, tenP, 0, 0, 0))
                        continue
                    for fiveP in range(0, 41):
                        if (200 * twoPounds + 100 * onePound + 50 * fiftyP + 20 * twentyP + 10 * tenP + 5 * fiveP == 200):
                            solutions.add((twoPounds, onePound, fiftyP, twentyP, tenP, fiveP, 0, 0))
                            continue
                        for twoP in range(0, 101):
                            if (200 * twoPounds + 100 * onePound + 50 * fiftyP + 20 * twentyP + 10 * tenP + 5 * fiveP + 2 * twoP == 200):
                                solutions.add((twoPounds, onePound, fiftyP, twentyP, tenP, fiveP, twoP, 0))
                                continue
                            for oneP in range(0, 201):
                                if (200 * twoPounds + 100 * onePound + 50 * fiftyP + 20 * twentyP + 10 * tenP + 5 * fiveP + 2 * twoP + oneP == 200):
                                    solutions.add((twoPounds, onePound, fiftyP, twentyP, tenP, fiveP, twoP, oneP))
                                    

print(len(solutions))