def solution(x, y, n):
    pre_set = set()
    pre_set.add(x)
    count = 0
    while pre_set:

        if y in pre_set:
            return count
        
        new_set = set()
        for num in pre_set:
            if num + n <= y:
                new_set.add(num + n)
            if num * 2 <= y:
                new_set.add(num * 2)
            if num * 3 <= y:
                new_set.add(num * 3)
        
        pre_set = new_set
        count += 1
    return -1