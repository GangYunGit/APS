# BOJ_1244

import sys
sys.stdin = open('input.txt')


def switch(num):
    if switch_state[num] == 1:
        switch_state[num] = 0
    else:
        switch_state[num] = 1


num_of_switch = int(input())
switch_state = list(map(int, input().split()))
switch_state.insert(0, 0)

num_of_student = int(input())
student_info = [list(map(int, input().split())) for _ in range(num_of_student)]

for student in student_info:
    if student[0] == 1:
        for i in range(student[1], num_of_switch + 1, student[1]):
            switch(i)

    elif student[0] == 2:
        switch(student[1])
        check = 1
        while True:
            if student[1] - check == 0 or student[1] + check == num_of_switch + 1:
                break

            if switch_state[student[1] - check] == switch_state[student[1] + check]:
                switch(student[1] - check)
                switch(student[1] + check)
            else:
                break

            check += 1

for i in range(1, len(switch_state)):
    print(switch_state[i], end=' ')
    if i % 20 == 0:
        print()