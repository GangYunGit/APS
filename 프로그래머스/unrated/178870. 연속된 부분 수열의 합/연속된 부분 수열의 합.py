from collections import deque

def solution(sequence, k):
    answer = []
    length = len(sequence)
    part_list = deque()
    sum_part = 0
    first_index, last_index = 0, 0
    length_compare = 1000000
    for i in range(length - 1, -1, -1):
        part_list.append(sequence[i])
        sum_part += sequence[i]
        first_index = i
        if sum_part >= k:
            if sum_part == k:
                last_index = i + len(part_list) - 1
                if len(part_list) <= length_compare:
                    length_compare = len(part_list)
                    answer = [first_index, last_index]
                # print(part_list, first_index, last_index)
            sum_part -= part_list.popleft()
    
    return answer