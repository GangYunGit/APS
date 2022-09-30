import sys
sys.stdin = open('input.txt', encoding='utf-8')
input = sys.stdin.readline


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


N = int(input())
planet_list = [list(map(int, input().split())) + [_] for _ in range(N)]
planet_info = []
parent = [_ for _ in range(N)]
cost = 0
count = 0

for point in range(3):
    planet_list.sort(key=lambda x: x[point])

    for i in range(N - 1):
        planet_distance = min(abs(planet_list[i][0] - planet_list[i + 1][0]), abs(planet_list[i][1] - planet_list[i + 1][1]), abs(planet_list[i][2] - planet_list[i + 1][2]))
        edge = (planet_list[i][3], planet_list[i + 1][3], planet_distance)
        planet_info.append(edge)

planet_info.sort(key=lambda x: x[2])
for planet in planet_info:
    root_a = find_set(planet[0])
    root_b = find_set(planet[1])

    if root_a != root_b:
        parent[root_b] = root_a
        cost += planet[2]
        count += 1

    if count >= N - 1:
        break

print(cost)
