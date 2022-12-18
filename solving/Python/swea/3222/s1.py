# SWEA_3233. 정삼각형 분할 놀이

for test_case in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    divided = A // B
    print(f'#{test_case} {divided ** 2}')