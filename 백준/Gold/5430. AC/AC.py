from collections import deque


def pop_func(is_reverse, num_list):
    if is_reverse:
        num_list.pop()
    else:
        num_list.popleft()


for test_case in range(1, int(input()) + 1):
    p = input()
    n = int(input())
    nums = input()
    nums = nums.replace('[', '').replace(']', '')

    if n == 0:
        num_list = deque()
    else:
        num_list = deque(nums.split(','))

    p = p.replace('RR', '')
    is_reverse = False
    empty_pop = 0
    a = len(p)

    for i in range(a):
        if p[i] == 'D':
            if not num_list:
                empty_pop = 1
                break
            else:
                pop_func(is_reverse, num_list)
                n -= 1
        else:
            is_reverse = not is_reverse

    if not num_list:
        if empty_pop == 1:
            print('error')
        else:
            print('[]')
    else:
        print('[', end='')
        if not is_reverse:
            for i in range(n):
                if i == n - 1:
                    print(f'{num_list[i]}]')
                else:
                    print(f'{num_list[i]},', end='')
        else:
            for i in range(n - 1, -1, -1):
                if i == 0:
                    print(f'{num_list[i]}]')
                else:
                    print(f'{num_list[i]},', end='')