# 1221_GNS

import sys
sys.stdin = open("input.txt", encoding="utf-8")

T = int(input())
for test_case in range(1, T + 1):
    test_num, test_length = input().split()
    sentence = input()
    i = 0
    string_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # 주어진 문장에서 string_num에 있는 특정 문자를 찾아 str(숫자)로 바꾸어줌
    for num in string_num:
        sentence = sentence.replace(num, str(i))
        i += 1

    # split 메서드를 사용하여 7 4 0... 문자열을 ["7", "4", "0",...] 배열로 변환 후, 오름차순 정렬
    sentence = sorted(sentence.split())

    # .join 메서드를 사용하여 다시 긴 문장으로 반환
    sentence = ' '.join(sentence)

    # 긴 문장의 각 숫자를 다시 외계어로 변경
    for i in range(10):
        for num in string_num:
            sentence = sentence.replace(str(i), string_num[i])

    print(f'#{test_case} {sentence}')



