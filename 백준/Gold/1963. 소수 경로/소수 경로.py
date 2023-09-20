from collections import deque


def is_prime(n):
    return sieve[n]


def change_prime(n):
    result = []
    for i in range(4):
        check_num = n - ((n // 10 ** i) % 10) * 10 ** i
        for j in range(10):
            switch_num = check_num + (10 ** i) * j
            if switch_num > 1000 and is_prime(switch_num):
                result.append(switch_num)

    return result


def bfs(before, after):
    visited = [False] * 10000
    queue = deque()
    depth = 0
    queue.append((before, depth))
    visited[before] = True

    while queue:
        num, depth = queue.popleft()
        if num == after:
            return depth

        for n in change_prime(num):
            if not visited[n]:
                visited[n] = True
                queue.append((n, depth + 1))

    return 'impossible'


m = int(10000 ** 0.5)
sieve = [True] * 10000
for i in range(2, m + 1):
    if sieve[i]:
        for j in range(2 * i, 10000, i):
            sieve[j] = False
prime_list = [_ for _ in range(1000, 10000) if sieve[_]]


for _ in range(int(input())):
    before, after = map(int, input().split())
    print(bfs(before, after))