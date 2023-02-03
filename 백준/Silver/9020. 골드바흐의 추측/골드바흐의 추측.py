import sys
input = sys.stdin.readline

num_list = [_ for _ in range(1, 10001)]
no_prime_list = []

for i in range(2, 10000):
    j = 2
    while i * j <= 10000:

        no_prime_list.append(i * j)
        j += 1

no_prime_list_set = set(no_prime_list)
num_list_set = set(num_list)
prime_list_set = num_list_set - no_prime_list_set


for test_case in range(1, int(input()) + 1):
    num = int(input())
    result_list = []
    result1, result2 = 0, 0
    min_subtract = 10000

    for prime_num in prime_list_set:
        compare_num = num
        new_prime = compare_num - prime_num

        if new_prime in prime_list_set:
            if prime_num <= new_prime:
                result_list.append((prime_num, new_prime))

    for prime1, prime2 in result_list:
        if prime2 - prime1 < min_subtract:
            min_subtract = prime2 - prime1
            result1, result2 = prime1, prime2

    print(result1, result2)