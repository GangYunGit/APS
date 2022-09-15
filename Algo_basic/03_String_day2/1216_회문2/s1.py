# 1216_회문2

import sys
sys.stdin = open("input.txt", encoding="utf-8")


def palindrome(grid):
    get_palindrome = ''
    max_val = ''
    for j in range(1, 102):
        for k in range(100):
            for i in range(100):
                # 행을 순서대로 0~99까지 탐색 후, 행의 길이를 1씩 줄여 나가면서 가능한 경우의 수 만큼 탐색.
                # ex) 행의 길이가 98이라면 0~97, 1~98, 2~99를 탐색
                if grid[i][k:j:] == grid[i][k:j:][::-1]:
                    get_palindrome = grid[i][k:j:]
                    break
            if len(get_palindrome) > len(max_val):
                max_val = get_palindrome
    return max_val


for test_case in range(1, 11):
    N = int(input())
    board = [input() for _ in range(100)]
    board_90 = list(map(list, zip(*board))) # 열방향을 검색하기 위해 행렬을 전치
    max_col_str = ''
    result = ''

    # 함수를 사용하여 행 방향과 열 방향의 최대 길이 회문을 각각 찾아줌
    max_row = palindrome(board)
    max_col = palindrome(board_90)

    # zip을 수행한 결과가 2차원 배열로 되어있어서 배열을 풀고 문자열로 바꿔주는 과정
    for char in max_col:
        max_col_str += char

    # 가장 긴 회문을 비교
    if len(max_row) > len(max_col_str):
        result = max_row
    else:
        result = max_col_str

    print(f'#{test_case} {len(result)}')
