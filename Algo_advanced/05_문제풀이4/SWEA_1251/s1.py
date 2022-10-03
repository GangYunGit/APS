# SWEA_1251_하나로

import sys
sys.stdin = open('input.txt')


def find_set(island):
    if island != parent[island]:
        parent[island] = find_set(parent[island])
    return parent[island]


for test_case in range(1, int(input()) + 1):
    N = int(input())
    island_i = list(map(int, input().split()))
    island_j = list(map(int, input().split()))
    E = float(input())
    adj_list = []
    parent = [_ for _ in range(N)]
    cost = 0
    count = 0

    for i in range(N):
        for j in range(N):
            if i != j:
                distance = (island_i[i] - island_i[j]) ** 2 + (island_j[i] - island_j[j]) ** 2
                adj_list.append((distance, i, j))
    adj_list.sort()

    for weight, start, end in adj_list:
        root_1, root_2 = find_set(start), find_set(end)

        if root_1 != root_2:
            cost += E * weight
            count += 1
            parent[root_2] = root_1

        if count >= N - 1:
            break

    print(f'#{test_case} {round(cost)}')