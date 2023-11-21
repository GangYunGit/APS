di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(i, j, num, depth):
    num.append(board[i][j])
    get_num = "".join(num)
    if depth == 5:
        if get_num not in num_set:
            num_set.add(get_num)
        return

    for direction in range(4):
        ni, nj = i + di[direction], j + dj[direction]
        if 0 <= ni < 5 and 0 <= nj < 5:
            depth += 1
            dfs(ni, nj, num, depth)
            num.pop()
            depth -= 1


board = [list(input().split()) for _ in range(5)]
num_set = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, [], 0)
print(len(num_set))