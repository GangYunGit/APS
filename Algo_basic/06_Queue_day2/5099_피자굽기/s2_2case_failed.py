# 5099_피자굽기 (테케 2개 틀림)
from collections import deque

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    oven_size, pizza_num = map(int, input().split())
    cheese_list = list(map(int, input().split()))

    oven = deque([0] * oven_size)
    pizza_index = deque([_ for _ in range(oven_size)])

    for i in range(oven_size):
        oven.popleft()
        oven.append(cheese_list[i])
        # print(oven, pizza_index)

    # print('시작')
    # print(oven, pizza_index)
    next_pizza = 1
    while next_pizza <= pizza_num - oven_size:
        for _ in range(oven_size):
            half_cheese = oven.popleft() // 2
            oven.append(half_cheese)
            pizza_index.append(pizza_index.popleft())
            # print(oven, pizza_index)

            if oven[oven_size - 1] == 0:
                oven[oven_size - 1] = cheese_list[oven_size - 1 + next_pizza]
                pizza_index[oven_size - 1] = oven_size - 1 + next_pizza
                next_pizza += 1
                # print(oven, pizza_index)
                break

    for _ in range(oven_size):
        half_cheese = oven.popleft() // 2
        oven.append(half_cheese)
        pizza_index.append(pizza_index.popleft())
        # print(oven, pizza_index)

    max_val = 0
    max_idx = 0
    for idx in range(len(oven)):
        if oven[idx] >= max_val:
            max_val = oven[idx]
            max_idx = idx

    print(f'#{test_case} {pizza_index[max_idx] + 1}')
