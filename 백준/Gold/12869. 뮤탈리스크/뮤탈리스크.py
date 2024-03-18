from collections import deque
from itertools import permutations


def attack_methods(scv_num):
    default_power = [9, 3, 1]
    return permutations(default_power, scv_num)


def bfs(scv_info):
    queue = deque()
    queue.append((scv_info, 0))
    visited = [[[False for _ in range(61)] for _ in range(61)] for _ in range(61)]
    visited[scv_info[0]][scv_info[1]][scv_info[2]] = True
    while queue:
        current_scv, depth = queue.popleft()
        count = 0
        for i in range(n):
            if current_scv[i] == 0:
                count += 1
        if count == n:
            return depth
        for attack_method in attack_methods(n):
            scv_hp = current_scv[:]
            for i in range(n):
                scv_hp[i] -= attack_method[i]
                if scv_hp[i] < 0:
                    scv_hp[i] = 0

            if visited[scv_hp[0]][scv_hp[1]][scv_hp[2]]:
                continue
            visited[scv_hp[0]][scv_hp[1]][scv_hp[2]] = True
            queue.append((scv_hp, depth + 1))


n = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:
    scv.append(0)
print(bfs(scv))