# 4839_이진탐색

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    page_total, page_a, page_b = map(int, input().split())
    left_a, right_a = 1, page_total # a가 찾을 페이지의 왼쪽, 오른쪽 값 설정
    left_b, right_b = 1, page_total # b가 찾을 페이지의 왼쪽, 오른쪽 값 설정
    find_a, find_b = 0, 0   # a, b가 찾은 중간의 값을 저장
    result = 0

    while True:
        # 중간의 값을 찍을 위치 설정
        find_a = (left_a + right_a) // 2

        # 탐색한 중간의 값이 목표값보다 작다면 왼쪽 페이지를 탐색한 값으로 재설정
        if find_a < page_a:
            left_a = find_a

        # 탐색한 중간의 값이 목표값보다 크다면 오른쪽 페이지를 탐색한 값으로 재설정
        else:
            right_a = find_a

        # b의 경우도 마찬가지.
        find_b = (left_b + right_b) // 2
        if find_b < page_b:
            left_b = find_b
        else:
            right_b = find_b

        # 비긴경우
        if find_a == page_a and find_b == page_b:
            result = 0
            break

        # A가 이긴경우
        if find_a == page_a:
            result = 'A'
            break

        # B가 이긴경우
        if find_b == page_b:
            result = 'B'
            break

    print(f'#{test_case} {result}')

