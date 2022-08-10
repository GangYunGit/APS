# 1954_달팽이_숫자

T = int(input())

for test_case in range(1, T + 1):
    loop_count = 0
    count = 0
    N = int(input())
    list_a = [[0]*N for i in range(N)]

    di = [0, 1, 0, -1]  # 하 상
    dj = [1, 0, -1, 0]  # 우 좌

    i = 0
    j = -1
    # j += dj[0] (4번) => i += di[1] (4번) -> j += dj[2] (4번) -> i += di[3] (3번)
    for drc in range((2*N-1) % 4):
        for k in range(N - drc//2):
            i += di[drc]
            j += dj[drc]
        print(i, j)








