def change_checker(word_1, word_2):
    count = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            count += 1
    if count == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False for _ in range(len(words))]
    min_length = len(words)
    route = []
    
    def dfs(begin):
        nonlocal min_length
        if len(route) > min_length:
            return
        
        if begin == target:
            min_length = len(route)
            return
            
        for i in range(len(words)):
            if change_checker(begin, words[i]) and not visited[i]:
                visited[i] = True
                route.append(words[i])
                dfs(words[i])
                route.pop()
                visited[i] = False
    
    dfs(begin)
    
    return min_length