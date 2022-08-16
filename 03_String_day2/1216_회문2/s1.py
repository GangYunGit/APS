# 1216_회문2

import sys
sys.stdin = open("input.txt", encoding="utf-8")

for test_case in range(1, 11):
    N = int(input())
    board = [input() for _ in range(100)]
    board_90 = list(map(list, zip(*board))) # 열방향을 검색하기 위해 행렬을 전치
    max_row = ''
    max_col = ''
    max_col_str = ''
    row_palindrome = ''
    col_palindrome = ''
    result = ''

    # 가로방향 탐색
    for j in range(101, 2, -1):
        for k in range(100):
            for i in range(100):
                # 행을 순서대로 0~99까지 탐색 후, 행의 길이를 1씩 줄여 나가면서 가능한 경우의 수 만큼 탐색.
                # ex) 행의 길이가 98이라면 0~97, 1~98, 2~99를 탐색
                if board[i][k:j:] == board[i][k:j:][::-1]:
                    row_palindrome = board[i][k:j:]
                if len(row_palindrome) > len(max_row):
                    max_row = row_palindrome

    # 세로방향 탐색(zip 으로 행렬을 90도 돌려 놓고 가로방향과 똑같은 코드로 진행)
    for j in range(101, 2, -1):
        for k in range(100):
            for i in range(100):
                if board_90[i][k:j:] == board_90[i][k:j:][::-1]:
                    col_palindrome = board_90[i][k:j:]
                if len(col_palindrome) > len(max_col):
                    max_col = col_palindrome

    # zip을 수행한 결과가 2차원 배열로 되어있어서 배열을 풀고 문자열로 바꿔주는 과정
    for char in max_col:
        max_col_str += char

    # 가장 긴 회문을 비교
    if len(max_row) > len(max_col_str):
        result = max_row
    else:
        result = max_col_str

    print(f'#{test_case} {len(result)}')