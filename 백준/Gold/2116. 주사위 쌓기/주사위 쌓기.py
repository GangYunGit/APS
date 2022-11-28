num_of_dice = int(input())
dice_list = [list(map(int, input().split())) for _ in range(num_of_dice)]
max_of_side_sum = 0

for choice in range(6):
    # print(dice_list)
    side_sum = 0
    for i in range(num_of_dice):
        sides = [1, 2, 3, 4, 5, 6]

        # 맨 아래에 있는 주사위의 윗 면(old_bottom *top값이 old_bottom에 들어감)과 바닥 면(next_bottom)을 구함
        if i == 0:
            next_bottom = dice_list[i][choice]
            if dice_list[i][choice] == next_bottom:
                if choice == 0:
                    top = dice_list[i][5]
                elif choice == 1:
                    top = dice_list[i][3]
                elif choice == 2:
                    top = dice_list[i][4]
                elif choice == 3:
                    top = dice_list[i][1]
                elif choice == 4:
                    top = dice_list[i][2]
                elif choice == 5:
                    top = dice_list[i][0]
                old_bottom = top
        # -------------------------------------------------------------------------------------------

        # 다음에 쌓인 주사위들의 윗면, 아랫면 값을 구함
        else:
            for choice2 in range(6):
                if dice_list[i][choice2] == next_bottom:
                    if choice2 == 0:
                        top = dice_list[i][5]
                    elif choice2 == 1:
                        top = dice_list[i][3]
                    elif choice2 == 2:
                        top = dice_list[i][4]
                    elif choice2 == 3:
                        top = dice_list[i][1]
                    elif choice2 == 4:
                        top = dice_list[i][2]
                    else:
                        top = dice_list[i][0]
            old_bottom = next_bottom
            next_bottom = top
        # -----------------------------------------------

        sides.remove(old_bottom)
        sides.remove(next_bottom)
        side_sum += max(sides)
        if side_sum >= max_of_side_sum:
            max_of_side_sum = side_sum
        # print(old_bottom, next_bottom)
        # print()

print(max_of_side_sum)
