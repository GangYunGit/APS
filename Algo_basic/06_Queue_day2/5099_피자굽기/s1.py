# 5099_피자굽기 (정답 풀이)

from collections import deque

import sys
sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    oven_size, pizza_num = map(int, input().split())
    cheese_list = list(map(int, input().split()))

    oven = deque([0] * oven_size)
    pizza_index = deque([_ for _ in range(oven_size)])

    # 오븐의 입구는 큐의 마지막 인덱스로 설정하고, 피자를 차례대로 오븐의 크기만큼 넣어줌
    for i in range(oven_size):
        oven.popleft()
        oven.append(cheese_list[i])

    # 마지막 피자가 화덕의 입구에 들어간 시점까지 반복을 진행
    next_pizza = 1
    while next_pizza <= pizza_num - oven_size:
        for _ in range(oven_size):
            half_cheese = oven.popleft() // 2
            oven.append(half_cheese)
            pizza_index.append(pizza_index.popleft())

            if oven[oven_size - 1] == 0:
                oven[oven_size - 1] = cheese_list[oven_size - 1 + next_pizza]
                pizza_index[oven_size - 1] = oven_size - 1 + next_pizza
                next_pizza += 1
                break

    # 모든 피자가 화덕에서 구워졌거나 구워지는 중이므로, 남은 피자들은 모두 한 바퀴씩 돌려서 꺼내기만 하면 됨
    while True:
        half_cheese = oven.popleft() // 2
        oven.append(half_cheese)
        pizza_index.append(pizza_index.popleft())

        # 오븐에서 마지막 피자가 나가는 순간 break
        if oven == deque([0] * oven_size):
            break

    print(f'#{test_case} {pizza_index[oven_size - 1] + 1}')
