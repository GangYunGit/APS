import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
sections = [list(map(int, input().split())) for _ in range(m)]

for i in range(1, n + 1):
    a[i] = a[i] + a[i - 1]

for section in sections:
    print(a[section[1]] - a[section[0] - 1])