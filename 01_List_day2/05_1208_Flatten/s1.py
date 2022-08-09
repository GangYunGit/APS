# 1208_Flatten

def max_and_min(num_list):  # 최댓값, 최솟값을 찾기 위한 함수
    max_val = 0
    min_val = 100
    for i in range(len(num_list)):
        if num_list[i] > max_val:
            max_val = num_list[i]
        if num_list[i] < min_val:
            min_val = num_list[i]
    return max_val, min_val


for test_case in range(1, 11):
    dump_times = int(input())
    box_list = list(map(int, input().split()))

    for dump in range(dump_times):  # dump를 수행
        max_num, min_num = max_and_min(box_list)    # 최댓값, 최솟값을 저장

        for j in range(len(box_list)):  # 모든 박스를 탐색하면서 가장 긴 첫번째 값을 찾으면 한 칸을 빼주고 break
            if box_list[j] == max_num:
                box_list[j] -= 1
                break

        for k in range(len(box_list)):  # 모든 박스를 탐색하면서 가장 짧은 첫번째 값을 찾으면 한 칸을 더해주고 break
            if box_list[k] == min_num:
                box_list[k] += 1
                break

        max_num, min_num = max_and_min(box_list)    # 최댓값, 최솟값을 출력하기 전에 최신화

    print(f'#{test_case} {max_num - min_num}')
