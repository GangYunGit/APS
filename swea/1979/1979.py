from operator import is_


T = int(input())


for test_case in range(1, T + 1):
    puzzle = []
    able = 0
    is_K = 0

    N, K = map(int, input().split())

    for puzzle_size in range(0, N):
        puzzle_row = list(map(str, input().split()))
        puzzle.append(puzzle_row)

    for row in range(N):
        count = 0
        for column in range(N):
            if puzzle[row][column] == '1':
                count += 1
            else:
                if count == K:
                    is_K += 1
                count = 0
        if count == K:
            is_K += 1

    for column in range(N):
        count = 0
        for row in range(N):
            if puzzle[row][column] == '1':
                count += 1
            else:
                if count == K:
                    is_K += 1
                count = 0
        if count == K:
            is_K += 1

    print(f'#{test_case} {is_K}')
