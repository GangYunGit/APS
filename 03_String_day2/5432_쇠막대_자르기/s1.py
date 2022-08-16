# 5432_쇠막대기_자르기

import sys
sys.stdin = open("input.txt")

T = int(input())
count = 0

for test_case in range(1, T + 1):
    steel_bar = input()
    laser = steel_bar.replace("()", '.')

    print(laser)
    if laser.count("(.)") > 0:
        count += laser.count("(.)")
        laser = laser.replace("(.)", ".")

    print(laser, count)