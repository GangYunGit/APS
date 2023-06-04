def solution(s):
    answer = []
    temp_num = ""
    s = s.lstrip("{{").rstrip("}}").split("},{")
    for i in range(len(s)):
        s[i] = set(map(int, s[i].split(",")))
        
    s.sort(key=lambda x: len(x))
    answer.append((s[0] - set()).pop())
    for i in range(len(s) - 1):
        get_item = (s[i + 1] - s[i]).pop()
        answer.append(get_item)
    
    return answer