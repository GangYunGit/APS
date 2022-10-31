# BOJ_9020. 골드바흐의 추측

import sys
input = sys.stdin.readline

prime_list = []
for i in range(1, 10000):
    prime_count = 0
    for divider in range(1, i + 1):
        mod = i % divider
        if mod == 0:
            prime_count += 1

    if prime_count == 2:
        prime_list.append(i)

for test_case in range(1, int(input()) + 1):
    num = int(input())
    result_list = []
    result1, result2 = 0, 0
    min_subtract = 10000

    for prime_num in prime_list:
        compare_num = num
        new_prime = compare_num - prime_num

        if new_prime in prime_list:
            if prime_num <= new_prime:
                result_list.append((prime_num, new_prime))

    for prime1, prime2 in result_list:
        if prime2 - prime1 < min_subtract:
            min_subtract = prime2 - prime1
            result1, result2 = prime1, prime2

    print(result1, result2)




