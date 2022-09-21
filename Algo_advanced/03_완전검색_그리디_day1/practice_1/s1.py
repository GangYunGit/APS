# 선택정렬 함수
def selection_sort(arr, start):

    if start == len(arr) - 1:          # 마지막 한 칸은 정렬 수행이 의미가 없으므로
        return                         # 마지막의 바로 앞 칸까지 수행을 마치면 리턴

    min = start                                     # 반복문에서 최소값을 저장할 변수
    for i in range(start, len(arr)):                # 시작지점부터 마지막 인덱스까지 정렬 수행
        if arr[i] < arr[min]:                       # 오름차순 정렬이므로 최소값을 찾아감
            arr[min], arr[i] = arr[i], arr[min]     # 최소값이라고 판별되면 자리를 바꿈
            min = i                                 # 최소값을 최신화
        selection_sort(arr, start + 1)              # 다음 칸에 대하여 정렬을 계속 수행


A = [2, 4, 6, 1, 9, 8, 7, 0]
selection_sort(A, 0)
print(A)    # [0, 1, 2, 4, 6, 7, 8, 9]
