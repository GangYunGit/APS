# 1213_String

import sys
sys.stdin = open("input.txt", encoding="utf-8")

for test_case in range(1, 11):
    T = int(input())
    word = input()
    sentence = input()
    print(f'#{test_case} {sentence.count(word)}')