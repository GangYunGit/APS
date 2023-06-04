def solution(s):
    answer = []
    temp_num = ""
    subset = set()
    subset_list = []
    for i in s:
        if i.isdecimal():
            temp_num += i
        if i == '}' and temp_num:
            subset.add(int(temp_num))
            subset_list.append(subset)
            temp_num = ""
            subset = set()
        if i == ',' and temp_num:
            subset.add(int(temp_num))
            temp_num = ""
        
    subset_list.sort(key=lambda x: len(x))
    answer.append((subset_list[0] - set()).pop())
    for i in range(len(subset_list) - 1):
        get_item = (subset_list[i + 1] - subset_list[i]).pop()
        answer.append(get_item)
    
    return answer