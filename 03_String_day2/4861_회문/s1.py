# 4861_회문

import sys
sys.stdin = open("input.txt", encoding="utf-8")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    result = ''

    # 한 묶음을 오른쪽으로 1칸씩 움직이면서 검사
    for k in range(N - M + 1):

        # 이후 board의 첫 번째 인덱스를 i로 쓰는지, j로 쓰는지에 따라 방향이 달라짐
        for i in range(N):
            row_palindrome = ''
            col_palindrome = ''

            # k번째 부터 시작하여 M길이 만큼의 문자열을 검색
            for j in range(k, k + M):
                row_palindrome += board[i][j]   # 행방향
                col_palindrome += board[j][i]   # 열방향

            # 슬라이싱을 이용하여 뒤집은 문자열이 해당 문자열과 일치 시 palindrome
            if row_palindrome == row_palindrome[::-1]:
                result = row_palindrome
                break
            elif col_palindrome == col_palindrome[::-1]:
                result = col_palindrome
                break

    print(f'#{test_case} {result}')
