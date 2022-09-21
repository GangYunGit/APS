# 5188_최소합

import sys
sys.stdin = open('input.txt')

# 델타 방향(아래, 오른쪽)
di = [1, 0]
dj = [0, 1]


# 시작점을 정하여 델타 검색 수행
def move(start_i, start_j):
    global sum_board        # 숫자 판의 합을 저장할 변수
    global min_of_sum       # 합의 최소값을 저장할 변수

    # 좌표가 우 하단 일 때 return
    if start_i == N - 1 and start_j == N - 1:
        sum_list.append(sum_board)      # 경로상 숫자의 합을 저장
        if sum_board < min_of_sum:      # 최소값을 비교하여
            min_of_sum = sum_board      # min_of_sum 에 저장
        return

    # 계산 중간마다 최소값보다 커지면 중단(백트래킹)
    if sum_board >= min_of_sum:
        return

    # 델타 검색
    for k in range(2):
        next_i = start_i + di[k]
        next_j = start_j + dj[k]
        if 0 <= next_i < N and 0 <= next_j < N:     # 다음 좌표가 범위 내에 있다면
            sum_board += board[next_i][next_j]      # 숫자판의 숫자를 더해줌
            move(next_i, next_j)                    # 다음 숫자판으로 이동
            sum_board -= board[next_i][next_j]      # 이전으로 되돌아갈 때 더했던 숫자를 빼서 원상복구


for test_case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    sum_board = board[0][0]         # 시작점의 숫자를 더해놓고 시작
    min_of_sum = 10 * 13 * 13       # 판의 최대 크기 : 13 x 13, 각 판의 숫자의 최대값 : 10
    move(0, 0)                      # [0][0]에서 함수를 수행

    print(f'#{test_case} {min(sum_list)}')      # 숫자판의 합들 중 최소값을 구함
