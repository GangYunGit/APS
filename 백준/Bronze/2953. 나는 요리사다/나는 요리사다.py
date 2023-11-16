print(*sorted([[i + 1, sum(map(int, input().split()))] for i in range(5)], key=lambda x: (x[1], x[0]))[-1])
