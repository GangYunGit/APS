# 4834_숫자_카드

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a_i = int(input())
    max_value = 0
    max_num = 0
    card_list = [0] * N
    card_slot = [0] * 10

    for i in range(N - 1, -1, -1):
        card_list[i] = a_i % 10
        a_i //= 10

    for i in range(N):
        card_slot[card_list[i]] += 1

    for i in range(len(card_slot)):
        if card_slot[i] >= max_value:
            max_value = card_slot[i]
            max_num = i

    print(f'#{test_case} {max_num} {max_value}')





