def integral(ranges, wobak):
    start, end = ranges[0], len(wobak) + ranges[1]
    result = 0
    if start >= end:
        return -1
    for i in range(start, end - 1):
        high = max(wobak[i], wobak[i + 1])
        low = min(wobak[i], wobak[i + 1])
        result += low + (high - low) / 2
    return result

        
def solution(k, ranges):
    answer = []
    wobak = [k] 
    while k != 1:
        if k % 2:
            k *= 3
            k += 1
        else:
            k //= 2
        wobak.append(k)
    
    for item in ranges:
        answer.append(integral(item, wobak))
    
    return answer