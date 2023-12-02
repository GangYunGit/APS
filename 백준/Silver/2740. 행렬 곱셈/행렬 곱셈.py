a_row, a_col = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(a_row)]
b_row, b_col = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(b_row)]
b = list(map(list, zip(*b)))
c = [[0] * b_col for _ in range(a_row)]
for i in range(a_row):
    for j in range(b_col):
        temp = 0
        for idx in range(a_col):
            temp += a[i][idx] * b[j][idx]
        c[i][j] = temp

for line in c:
    print(*line, end="\n")