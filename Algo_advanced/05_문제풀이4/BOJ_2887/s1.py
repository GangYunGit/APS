from itertools import combinations

import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


N = int(input())
planet_list = [list(map(int, input().split())) for _ in range(N)]
parent = [_ for _ in range(N)]

edge_info = list(combinations(parent, 2))
planet_info = []
cost = 0
count = 0

for start, end in edge_info:
    planet_a = planet_list[start]
    planet_b = planet_list[end]
    cost = min(abs(planet_a[0] - planet_b[0]), abs(planet_a[1] - planet_b[1]), abs(planet_a[2] - planet_b[2]))
    planet_info.append((start, end, cost))

planet_info.sort(key=lambda x: x[2])
print(planet_info)
for planet in planet_info:
    root_a = find_set(planet[0])
    root_b = find_set(planet[1])

    if root_a != root_b:
        parent[root_b] = root_a
        cost += planet[2]
        count += 1

    if count == N:
        break

print(cost)



