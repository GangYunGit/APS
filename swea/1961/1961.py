T = int(input())

for test_case in range(T):
    N = int(input())
    shape = []
    shape_90 = []
    shape_180 = []
    shape_270 = []
    trans_shape = []

    for i in range(N):
        row = list(map(str, input().split()))
        shape.append(row)

    for i in range(N):
        new_shape = ''
        for j in range(N - 1, -1, -1):
            new_shape += shape[j][i]
        shape_90.append(new_shape)
    trans_shape.append(shape_90)

    for i in range(N - 1, -1, -1):
        new_shape = ''
        for j in range(N - 1, -1, -1):
            new_shape += shape[i][j]
        shape_180.append(new_shape)
    trans_shape.append(shape_180)

    for i in range(N - 1, -1, -1):
        new_shape = ''
        for j in range(N):
            new_shape += shape[j][i]
        shape_270.append(new_shape)
    trans_shape.append(shape_270)

    new_trans_shape = list(map(list, zip(*trans_shape)))

    print(f'#{test_case + 1}')
    for i in range(N):
        for j in range(3):
            print(new_trans_shape[i][j], end=' ')
        print()
