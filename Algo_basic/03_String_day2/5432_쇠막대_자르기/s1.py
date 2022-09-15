# 5432_쇠막대기_자르기

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    steel_bar = input()
    steel_bar = steel_bar.replace("()", ".")
    laser = "(.)"
    laser_count = 2
    count = 0

    while steel_bar.count("(") != 0:
        while steel_bar.count(laser) != 0:
            count += laser_count * steel_bar.count(laser)
            steel_bar = steel_bar.replace(laser, laser.strip("(").strip(")"))
        laser = laser.replace(".)", "..)")
        laser_count += 1

    print(f'#{test_case} {count}')




    # print(laser)
    # if laser.count("(.)") > 0:
    #     count += laser.count("(.)") * 2
    #     laser = laser.replace("(.)", ".")
    # print(laser, count)
    #
    # if laser.count("(..)") > 0:
    #     count += laser.count("(..)") * 3
    #     laser = laser.replace("(..)", "..")
    # print(laser, count)
    #
    # if laser.count("(...)") > 0:
    #     count += laser.count("(...)") * 4
    #     laser = laser.replace("(...)", "...")
    # print(laser, count)
    #
    # if laser.count("(....)") > 0:
    #     count += laser.count("(....)") * 5
    #     laser = laser.replace("(....)", "....")
    # print(laser, count)
    #
    # if laser.count("(....)") > 0:
    #     count += laser.count("(....)") * 5
    #     laser = laser.replace("(....)", "....")
    # print(laser, count)
