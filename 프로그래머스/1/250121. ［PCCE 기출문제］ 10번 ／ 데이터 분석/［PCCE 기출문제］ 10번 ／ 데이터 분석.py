def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_info = ["code", "date", "maximum", "remain"]
    compare_idx = 0
    sort_idx = 0
    for i in range(4):
        if ext == ext_info[i]:
            compare_idx = i
        if sort_by == ext_info[i]:
            sort_idx = i
    
    for item in data:
        if item[compare_idx] < val_ext:
            answer.append(item)
    answer.sort(key=lambda x: x[sort_idx])
    
    return answer