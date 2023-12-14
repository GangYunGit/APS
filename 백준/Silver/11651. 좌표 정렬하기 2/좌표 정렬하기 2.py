num = [list(map(int, input().split())) for _ in range(int(input()))]
for a, b in sorted(num, key=lambda x: (x[1], x[0])):
    print(a, b)