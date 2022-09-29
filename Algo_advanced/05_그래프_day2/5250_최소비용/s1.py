# 5250_최소비용

import sys
sys.stdin = open('input.txt')


def find_set(i, j):
    if (i, j) != parent[i][j]:
        parent[i][j][0] = find_set(parent[i][j][0])
    return parent[i][j][0]


# 좌, 상, 우, 하
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]


for test_case in range(1, int(input()) + 1):
    size = int(input())
    height_list = [list(map(int, input().split())) for _ in range(size)]
    total_fuel = 0

    adj_list = [[] * (size ** 2 + 1)]

    for i in range(1, size ** 2 + 1):
        adj_list.append((i, ))






