from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine_counter = Counter(tangerine)
    box_size = 0
    for size in sorted(tangerine_counter.values(), reverse=True):
        if box_size < k:
            box_size += size
            answer += 1
        else:
            break
    
    return answer