# BOJ_1764. 듣보잡
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
hear = set()
look = set()
result = []

for _ in range(N):
    hear.add(input().rstrip())

for _ in range(M):
    look.add(input().rstrip())

result = sorted(list(hear & look))
print(len(result))
print(*result, sep='\n')
