from collections import defaultdict

def solution(gems):
    gem_types = set(gems)
    gems_dict = defaultdict(int)
    results = []
    start, end = 0, 0
    while True:
        if start == len(gems):
            break 
        
        if len(gems_dict) == len(gem_types):
            results.append((start, end))
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] <= 0:
                gems_dict.pop(gems[start], None)
            start += 1
            continue
        
        if end == len(gems):
            break
        
        if len(gems_dict) != len(gem_types):
            gems_dict[gems[end]] += 1
            end += 1
            
    min_gap = 100000
    min_s, min_e = 100000, 100000
    for s, e in results:
        if e - s < min_gap:
            min_gap = e - s
            min_s = s
            min_e = e     
    
    answer = [min_s + 1, min_e]
        
    return answer