def dfs(size, matrix):
    if size <= 1:
        print(matrix[0][0])
        return
    new_size = size // 2
    new_matrix = [[] for _ in range(new_size)]
    for i in range(0, size, 2):
        for j in range(0, size, 2):
            check_list = []
            for i_gap in range(2):
                for j_gap in range(2):
                    row = i + i_gap
                    col = j + j_gap
                    check_list.append(matrix[row][col])
            get_second_num = sorted(check_list)[-2]
            new_matrix[i // 2].append(get_second_num)
    dfs(new_size, new_matrix)


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dfs(n, matrix)