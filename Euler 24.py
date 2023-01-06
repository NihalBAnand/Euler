from itertools import permutations
digits = "0123456789"
print([''.join(perm) for perm in permutations(digits)][999999])