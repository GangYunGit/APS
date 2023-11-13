n, m = map(int, input().split())
bread = [list(input()) for _ in range(n)]
for i in range(n):
    print("".join(bread[i][::-1]))