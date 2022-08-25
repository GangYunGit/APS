# 5099_피자굽기
from collections import deque

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    oven_size, pizza_num = map(int, input().split())
    cheese_list = list(map(int, input().split()))

    cheese_dict = {i + 1: cheese_list[i] for i in range(pizza_num)}
    oven = deque([])
    pizza_index = deque([_ + 1 for _ in range(oven_size)])
    last_pizza = oven_size
    # 오븐 안에 피자를 넣음
    for i in range(1, oven_size + 1):
        oven.append(cheese_dict[i])
    print()
    print('시작')
    print(oven, pizza_index)
    # 치즈를 줄이자
    for plus in range(pizza_num - oven_size + 1):
        for _ in range(oven_size):
            half_cheese = oven.popleft() // 2
            oven.append(half_cheese)
            pizza_index.append(pizza_index.popleft())
            if oven[0] == 0:
                oven[0] = cheese_dict[oven_size + plus]
                last_pizza += 1
                pizza_index[0] = last_pizza
                print('다음 피자 넣기')
            print(oven, pizza_index)
        print(f'{plus + 1}사이클 : {oven} {pizza_index}')



        # if oven == deque([0] * oven_size):
        #     print(oven)
        #     break








