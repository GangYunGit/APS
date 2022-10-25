# BOJ_11866. 요세푸스 문제0

from collections import deque

N, K = map(int, input().split())
table = deque([_ for _ in range(1, N + 1)])

print('<', end='')

while table:
    table.rotate(-K)
    print(table.pop(), end=', ') if len(table) > 1 else print(table.pop(), end='')

print('>')
