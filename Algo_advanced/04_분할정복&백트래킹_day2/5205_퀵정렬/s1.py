# 5205_퀵정렬

import sys
sys.stdin = open('input.txt', encoding='utf-8')


# 파티션을 정해줄 함수
def partition(left, right):
    pivot = unsorted_list[left]         # 배열의 원소 중 하나를 pivot으로 정함
    i, j = left, right                  # pivot 값과 비교하여 왼쪽 혹은 오른쪽에 위치시키기 위한 변수

    while i <= j:
        while i <= j and unsorted_list[i] <= pivot:     # pivot 보다 작은 값을
            i += 1                                      # 인덱스가 증가하는 방향으로 확인
        while i <= j and unsorted_list[j] >= pivot:     # pivot 보다 큰 값을
            j -= 1                                      # 인덱스가 감소하는 방향으로 확인

        # i와 j가 교차하는 지점까지 pivot보다 큰 값과 pivot보다 작은 값을 교환
        if i < j:
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]

    # i와 j가 교차했다면 pivot과 pivot보다 큰 값(j)와 교환
    unsorted_list[left], unsorted_list[j] = unsorted_list[j], unsorted_list[left]
    return j


# 퀵 정렬
def quick_sort(left, right):
    if left < right:                        # 파티션에서 정의한 i와 j과 교차될 때까지 퀵정렬 수행
        swap = partition(left, right)       # i와 j가 교차되었을 때 j의 인덱스를 swap 변수에 저장
        quick_sort(left, swap - 1)          # 정렬이 끝난 후, 원소를 제외하고 pivot보다 큰 원소와
        quick_sort(swap + 1, right)         # pivot보다 작은 원소를 찾아가며 퀵정렬을 다시 수행


for test_case in range(1, int(input()) + 1):
    N = int(input())
    unsorted_list = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print(f'#{test_case} {unsorted_list[N // 2]}')
