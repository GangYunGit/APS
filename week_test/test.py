# 과목평가 대비


# # 버블 정렬
# list_a = [10, 24, 52, 32, 48, 99, 87, 63, 77]
# for i in range(len(list_a) - 1, 0, -1):
#     for j in range(i):
#         if list_a[j] > list_a[j + 1]:
#             list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]


# # 카운팅 정렬
# list_a = [10, 24, 52, 32, 48, 99, 87, 63, 77]
# temp = [0] * len(list_a)
# print(list_a)
# counter = [0] * 100
# for num in list_a:
#     counter[num] += 1
#
# for i in range(1, len(counter)):
#     counter[i] = counter[i - 1] + counter[i]
# print(counter)
#
# for i in range(len(list_a) - 1, -1, -1):
#     counter[list_a[i]] -= 1
#     temp[counter[list_a[i]]] = list_a[i]
#
# print(temp)

# # 선택 정렬
# list_a = [99, 87, 63, 77, 10, 24, 52, 32, 48]
#
# for i in range(len(list_a) - 1):
#     min_idx = i
#     for j in range(i, len(list_a)):
#         if list_a[j] < list_a[min_idx]:
#             min_idx = j
#     list_a[i], list_a[min_idx] = list_a[min_idx], list_a[i]
#
# print(list_a)


# # 이차원 배열 순회
# board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# for i in range(3):
#     for j in range(4):
#         print(board[i][j + ((4 - 1) - (2 * j))*(i % 2)], end=' ')
#     print()


# # 이진 탐색 1
# import sys
# sys.stdin = open('input.txt')
#
#
# def binary_search(page, total_page):
#     count = 0
#     find_page = 0
#     page_left = 0
#     page_right = total_page
#     while find_page != page:
#         find_page = (page_left + page_right) // 2
#         if find_page >= page:
#             page_right = find_page
#         else:
#             page_left = find_page
#         count += 1
#     return count
#
#
# for test_case in range(1, int(input()) + 1):
#     total_page, page_a, page_b = map(int, input().split())
#     count_a = 0
#     count_b = 0
#
#     count_a = binary_search(page_a, total_page)
#     count_b = binary_search(page_b, total_page)
#
#     print(count_a, count_b)


# 이진 탐색 2
target = int(input())

list_a = [40, 10, 23, 97, 54, 83, 73, 62, 36]
list_a.sort()

find = 0
left = 0
right = len(list_a)
while True:
    find = (left + right) // 2
    if list_a[find] >= target:
        right = find
    else:
        left = find
    print(left, right, list_a[find])
    if list_a[find] == target:
        print(left, right, list_a[find])
        break
    if right - left <= 1 and find != target:
        print('No')
        break

print(find)


# # Stack 구조
# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print("Stack Overflow!")
#     else:
#         stack[top] = item
#
#
# def pop():
#     global top
#     if top == -1:
#         print("Stack Underflow!")
#     else:
#         top -= 1
#         return stack[top + 1]
#
# # 스택 초기화
# top = -1
# size = 3
# stack = [0] * size
#
# push(1, size)
# push(2, size)
# push(3, size)
# print(stack)
#
# print(pop())
# print(pop())
# print(pop())
#
