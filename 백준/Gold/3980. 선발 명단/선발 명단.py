def dfs(row, current_point):
    global max_point
    if row == 11:
        max_point = max(max_point, current_point)
        return

    for col in range(11):
        if ability[row][col] > 0 and not visited[row][col] and not position[col]:
            visited[row][col] = True
            position[col] = True
            current_point += ability[row][col]
            dfs(row + 1, current_point)
            visited[row][col] = False
            position[col] = False
            current_point -= ability[row][col]


for _ in range(int(input())):
    ability = [list(map(int, input().split())) for _ in range(11)]
    visited = [[False] * 11 for _ in range(11)]
    position = [False] * 11
    max_point = 0
    dfs(0, 0)
    print(max_point)