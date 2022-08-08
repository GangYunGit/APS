T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    fly_cell = []
    M_rooms_list = []

    for row in range(N):
        fly = list(map(int, input().split()))
        fly_cell.append(fly)

    for row in range(N - M + 1):
        for column in range(N - M + 1):
            M_rooms = 0
            for i in range(M):
                for j in range(M):
                    M_rooms += fly_cell[row + i][column + j]
            M_rooms_list.append(M_rooms)

    print(f'{test_case} {max(M_rooms_list)}')
