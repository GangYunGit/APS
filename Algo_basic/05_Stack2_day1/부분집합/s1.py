# 부분집합

from itertools import permutations

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for powerset in permutations(list_a, 3):
    if sum(list(powerset)) == 10:
        print(list(powerset))
