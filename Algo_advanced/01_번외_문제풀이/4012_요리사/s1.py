# 4012_요리사
import sys
from itertools import combinations, permutations
sys.stdin = open('input.txt')


for test_case in range(1, int(input()) + 1):
    N = int(input())
    synergy_info = [list(map(int, input().split())) for _ in range(N)]

    pick = [0] * (N // 2)
    pick_list = []
    flavor_list = []
    idx = [i for i in range(1, N + 1)]
    comb_idx = list(combinations(idx, N // 2))
    for i in range(len(comb_idx) // 2):
        flavor_a = 0
        flavor_b = 0
        for a in permutations(comb_idx[i], 2):
            flavor_a += synergy_info[a[0] - 1][a[1] - 1]

        for b in permutations(comb_idx[len(comb_idx) - i - 1], 2):
            flavor_b += synergy_info[b[0] - 1][b[1] - 1]

        flavor_list.append(abs(flavor_a - flavor_b))
    print(f'#{test_case} {min(flavor_list)}')

