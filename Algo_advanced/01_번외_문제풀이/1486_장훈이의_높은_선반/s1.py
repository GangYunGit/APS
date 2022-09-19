# 1486_장훈이의_높은_선반

import sys
from itertools import combinations

sys.stdin = open('input.txt', encoding='utf-8')


for test_case in range(1, int(input()) + 1):
    staff, shelf = map(int, input().split())
    staff_height_list = list(map(int, input().split()))
    min_val = 20 * 10000    # 최악의 최소값 : 점원의 수 * 점원의 키의 최대값

    # 조합의 길이가 직원이 1명일 때부터 최대일 때까지 반복
    for i in range(1, staff + 1):
        tower = 0       # 쌓은 탑의 높이를 저장할 변수
        
        # 만들어진 모든 경우의 수의 조합에서
        for comb in combinations(staff_height_list, i):
            tower = sum(comb)           # 직원의 키를 모두 더하여 타워의 높이를 구함
            compare = tower - shelf     # 탑과 선반의 높이의 차이
            if compare >= 0:            # 탑과 선반의 높이의 차이가 0이상이면
                if compare < min_val:   
                    min_val = compare   # 탑과 선반의 높이 차이의 최소값을 저장

    print(f'#{test_case} {min_val}')
