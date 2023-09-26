def square_check(i, j):
    num = rectangle[i][j]
    count = 1
    result = 1
    while True:
        if i + count >= n or j + count >= m:
            break

        if num == rectangle[i + count][j] and num == rectangle[i][j + count] and num == rectangle[i + count][j + count]:
            result = (count + 1) ** 2
        count += 1

    return result


n, m = map(int, input().split())
rectangle = [list("".join(input())) for _ in range(n)]
max_size = 0

for i in range(n):
    for j in range(m):
        max_size = max(square_check(i, j), max_size)

print(max_size)