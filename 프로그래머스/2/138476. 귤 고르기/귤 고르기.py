def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    tangerine_size = []
    prev = tangerine[0]
    count = 1
    if len(tangerine) == 1:
        tangerine_size.append((1, prev))
    
    for i in range(1, len(tangerine)):
        if prev == tangerine[i]:
            count += 1
        else:
            tangerine_size.append((count, prev))
            count = 1
            prev = tangerine[i]
            
        if i == len(tangerine) - 1:
            tangerine_size.append((count, tangerine[i]))
    
    tangerine_size.sort(reverse=True)

    box_size = 0
    for num, tangerine_idx in tangerine_size:
        if box_size < k:
            box_size += num
            answer += 1
        else:
            break
            
    return answer