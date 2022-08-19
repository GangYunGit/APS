# 3449_퍼펙트_셔플

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    my_deck = list(map(str, input().split()))
    shuffle_1 = []
    shuffle_2 = []
    shuffled_deck = []

    if N % 2:
        for i in range(0, N//2 + 1):
            shuffle_1.append(my_deck[i])

        for j in range(N//2 + 1, N):
            shuffle_2.append(my_deck[j])

        for k in range(N//2):
            shuffled_deck.append(shuffle_1[k])
            shuffled_deck.append(shuffle_2[k])
        shuffled_deck.append(shuffle_1[N//2])
    else:
        for i in range(0, N//2):
            shuffle_1.append(my_deck[i])

        for j in range(N//2, N):
            shuffle_2.append(my_deck[j])

        for k in range(N//2):
            shuffled_deck.append(shuffle_1[k])
            shuffled_deck.append(shuffle_2[k])

    print(f'#{test_case}', end=' ')
    print(*shuffled_deck)

