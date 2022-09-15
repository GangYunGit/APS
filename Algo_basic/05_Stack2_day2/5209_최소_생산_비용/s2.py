# 5209_최소_생산_비용

import sys
sys.stdin = open('input.txt')


# 행을 기준으로 순열을 찾는 함수
def func(row, sum_val):
    global min_val      # 최소값을 지정할 변수
    global cnt          # 반복문 수행 횟수를 체크

    # !백트래킹이 있던 자리

    # 공장 한 개당 제품을 하나씩 모두 골라주었으면 함수를 호출스택에서 제거하고 다음 문장 실행
    if row == N:
        # 생산비용 합의 최소값을 최신화
        if sum_val < min_val:
            min_val = sum_val
        return

    # DFS 방식을 통해 행을 탐색
    for col in range(N):

        # 방문하지 않은 행을 탐색
        if not visited[col]:
            cnt += 1
            visited[col] = True     # 방문 했다는 표시
            sum_val += cost[row][col]   # 해당 칸의 비용을 더함

            func(row + 1, sum_val)  # 다음 행에 해당하는 열을 선택

            # 뒷걸음질을 친다고 생각해보자
            visited[col] = False    # 방문 표시를 제거하므로써 순서 쌍이 생길 수 있음 => 순열
            sum_val -= cost[row][col]   # 뒷걸음질을 쳤으니 이전에 수행했던 연산도 되돌려준다.


for test_case in range(1, int(input()) + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_val = N * 99 * 99   # 3 <= N <= 15, 1 <= 생산비용 <= 99에 맞추어 비교할 최소값을 초기화
    cnt = 0

    func(0, 0)      # 0번째 행, sum_val = 0에서 시작
    print(f'#{test_case} {min_val} \t 반복 횟수 : {cnt}')
