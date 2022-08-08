T = int(input())

for test_case in range(1, T + 1):
    puzzle = []
    puzzle_length = range(9)
    is_9 = 0
    confirmed = 0
    game = 0

    for i in puzzle_length:
        row = list(map(int, input().split()))
        puzzle.append(row)

    for i in puzzle_length:
        is_row = 0
        is_column = 0
        for j in puzzle_length:
            is_row += puzzle[i][j]
            is_column += puzzle[j][i]
        if is_row == 45 and is_column == 45:
            continue
        else:
            confirmed += 1

    for k_i in range(0, 9, 3):
        for k_j in range(0, 9, 3):
            is_9 = 0
            for i in range(3):
                for j in range(3):
                    is_9 += puzzle[i + k_i][j + k_j]
            if is_9 == 45:
                continue
            else:
                confirmed += 1

    if confirmed == 0:
        game = 1
    else:
        game = 0

    print(f'#{test_case} {game}')
