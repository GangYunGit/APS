# 1945_간단한_소인수분해

# import sys
# sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    N = int(input())
    factors = [2, 3, 5, 7, 11]  # 명세에 주어진 소인수들의 리스트

    for factor in factors:  # 소인수 하나를 순서대로 뽑아내서 반복문 진행
        count = 0   # 각 소인수의 지수를 계산해줄 변수
        while N % factor == 0:  # 소인수로 나누어 떨어지지 않을 때까지 반복
            N //= factor
            count += 1
        print(count, end=' ')
    print()