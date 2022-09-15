# 4865_글자수

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = input()
    M = input()
    list_N = list({_ for _ in N})   # set을 이용하여 중복을 제거 후 리스트로 형변환
    max_count = 0

    # str2를 돌면서 str1에 있는 문자가 나올 때마다 count
    for i in range(len(list_N)):
        count = 0
        for char_M in M:
            if list_N[i] == char_M:
                count += 1

        # count 값들 중 최대값을 비교
        if count > max_count:
            max_count = count

    print(f'#{test_case} {max_count}')
