# 1859_백만장자_프로젝트

import sys
sys.stdin = open('input.txt')

# input파일 용량이 커서 렉이 걸리는 문제는 처음이네요
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = 0
    count = 0

    # 지붕을 씌워준다는 느낌으로
    # 배열의 마지막 부분부터 접근.
    for i in range(len(price)-1, -1, -1):
        # 이전 값보다 큰 값을 만나면 max값을 갱신
        # 갱신이 되지 않는다면 높이는 변하지 않음
        if price[i] >= max_price:
            max_price = price[i]
        count += max_price - price[i]   # 지붕과 원래 가격의 차이만큼을 더해줌

    print(f'#{test_case} {count}')



