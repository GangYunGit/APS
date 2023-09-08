import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    number_list = sorted([input().strip() for _ in range(n)])
    result = 'YES'
    for i in range(n - 1):
        first_number = number_list[i]
        second_number = number_list[i + 1]
        if first_number == second_number[:len(first_number)]:
            result = 'NO'
            break
    print(result)