# 10773_제로

import sys
sys.stdin = open("input.txt")

K = int(input())
money_stack = []

for i in range(K):
    money = int(input())
    if money == 0:
        money_stack.pop()
    else:
        money_stack.append(money)

print(sum(money_stack))