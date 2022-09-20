# 4366_정식이의 은행업무

import sys
sys.stdin = open('input.txt', encoding='utf-8')


for test_case in range(1, int(input()) + 1):
    binary_num = int(input(), base=2)
    temp = input()
    a = [0, 1, 2]

    shifted_binary_num = 0
    shifted_binary_num_list = [binary_num]
    for i in range(len(bin(binary_num)[2:])):
        if binary_num & (1 << i):
            binary_num -= 1 << i
            shifted_binary_num = binary_num
            binary_num += 1 << i
        else:
            binary_num += 1 << i
            shifted_binary_num = binary_num
            binary_num -= 1 << i
        shifted_binary_num_list.append(shifted_binary_num)

    shifted_ternary_num_list = []
    ternary_num = ' '.join(temp).split()

    for i in range(len(ternary_num)):
        if ternary_num[i] == '2':
            ternary_num[i] = '1'
            new_ternary_num = ''.join(ternary_num)
            shifted_ternary_num_list.append(int(new_ternary_num, base=3))
            ternary_num[i] = '0'
            new_ternary_num = ''.join(ternary_num)
            shifted_ternary_num_list.append(int(new_ternary_num, base=3))
            ternary_num[i] = '2'
        elif ternary_num[i] == '1':
            ternary_num[i] = '0'
            new_ternary_num = ''.join(ternary_num)
            shifted_ternary_num_list.append(int(new_ternary_num, base=3))
            ternary_num[i] = '2'
            new_ternary_num = ''.join(ternary_num)
            shifted_ternary_num_list.append(int(new_ternary_num, base=3))
            ternary_num[i] = '1'
        else:
            ternary_num[i] = '1'
            new_ternary_num = ''.join(ternary_num)
            shifted_ternary_num_list.append(int(new_ternary_num, base=3))
            ternary_num[i] = '2'
            new_ternary_num = ''.join(ternary_num)
            shifted_ternary_num_list.append(int(new_ternary_num, base=3))
            ternary_num[i] = '0'

    result = 0
    for num1 in shifted_binary_num_list:
        for num2 in shifted_ternary_num_list:

            if num1 == num2:
                result = num1

    print(f'#{test_case} {result}')