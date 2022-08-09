# 4831_전기버스

T = int(input())

for test_case in range(1, T + 1):
    can_go, destination, charger_num = map(int, input().split())
    charger_list = list(map(int, input().split()))
    charger_row = [0] * (destination + 1)
    my_location = 0
    count = 0

    for i in charger_list:
        charger_row[i] += 1

    for j in range(destination, -1, -1):




    print(charger_row)



