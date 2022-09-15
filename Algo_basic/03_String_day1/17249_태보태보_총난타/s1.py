# 17249_태보태보_총난타

import sys
sys.stdin = open("input.txt")

T = input()
left_count = 0
right_count = 0

# .find메서드와 슬라이싱을 이용하여 '('의 오른쪽을 잘라냄
T_left = T[:T.find('(') + 1]

# .find메서드와 슬라이싱을 이용하여 ')'의 왼쪽을 잘라냄
T_right = T[T.find(')'):]

left_count = T_left.count('@=')     # 왼손의 잔상 카운트
right_count = T_right.count('=@')   # 오른손의 잔상 카운트

print(left_count, right_count)



