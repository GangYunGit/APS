n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
for i, j in sorted(points, key=lambda x:(x[0], x[1])):
    print(i, j, end="\n")