import sys
input = sys.stdin.readline


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


def is_not_cycle(node_1, node_2):
    root_1, root_2 = find_set(node_1), find_set(node_2)
    if root_1 != root_2:
        if root_1 < root_2:
            parent[root_2] = root_1
        else:
            parent[root_1] = root_2
        return True
    else:
        return False


N = int(input())
M = int(input())
computer_info = [list(map(int, input().split())) for _ in range(M)]
computer_info.sort(key=lambda x: x[2])

parent = [_ for _ in range(N + 1)]
cost = 0
count = 0

for start, end, distance in computer_info:
    if is_not_cycle(start, end):
        count += 1
        cost += distance

        if count == N - 1:
            break
print(cost)
