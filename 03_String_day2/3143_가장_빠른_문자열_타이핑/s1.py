# 3143. 가장 빠른 문자열 타이핑

import sys
sys.stdin = open("input.txt", encoding="utf-8")

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(str, input().split())
    count_string = ''
    result = 0
    
    # 문자열 A를 돌면서 문자열 B와 동일한 배열이 나오면 replace로 없애고, 결과를 +1
    for char_a in A:
        count_string += char_a  
        if count_string.count(B) == 1:
            result += 1
            count_string = count_string.replace(B, "")
    
    # 빠른 타이핑을 카운트하고 남은 문자열들을 하나씩 카운트
    for _ in count_string:
        result += 1

    print(f'#{test_case} {result}')


