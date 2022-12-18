# BOJ_5430. AC
from collections import deque


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

    for i in range(len(p)):
        if p[i] == 'D':
            if not num_list:
                print('error')
                break
            else:
                if is_reverse:
                    num_list.pop()
                else:
                    num_list.popleft()
                n -= 1
        else:
            is_reverse = not is_reverse

    else:
        if is_reverse:
            num_list.reverse()
        print('[', ','.join(num_list), ']', sep='')

'''
1
D
0
[]

1
RRRRRDD
4
[1,2,3,4]
'''


