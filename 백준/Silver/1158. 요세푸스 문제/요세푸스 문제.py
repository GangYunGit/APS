from collections import deque

N, K = map(int, input().split())
people = deque(i for i in range(1, N + 1))

print('<', end='')
for i in range(N):
    people.rotate(-K)
    if i == N - 1:
        print(people.pop(), end='')
    else:
        print(f'{people.pop()}, ', end='')
print('>')