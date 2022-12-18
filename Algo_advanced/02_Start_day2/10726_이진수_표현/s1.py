import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    count = 0
    result = ''
    for i in range(N):
        if M & (1 << i):
            count += 1

    if count == N:
        result = 'ON'
    else:
        result = 'OFF'

    print(f'#{test_case} {result}')