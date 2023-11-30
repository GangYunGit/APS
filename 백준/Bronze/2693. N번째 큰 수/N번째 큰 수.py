n = int(input())
for _ in range(n):
    print(sorted(list(map(int, input().split())))[-3])