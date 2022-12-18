# 5431_민석이의_과제_체크하기

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    no_homework = list(map(int, input().split()))

    student_list = [i + 1 for i in range(N)]

    for student in no_homework:
        student_list.remove(student)

    print(f'#{test_case}', end=' ')
    print(*student_list)