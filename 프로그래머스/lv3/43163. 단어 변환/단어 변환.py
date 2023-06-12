def change_checker(word_1, word_2):
    count = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = [False for _ in range(len(words))]
    route = []
    answer = len(words)
    
    def dfs(begin):
        nonlocal answer
        if len(route) > answer:
            return
        
        if begin == target:
            answer = len(route)
            return
            
        for i in range(len(words)):
            if change_checker(begin, words[i]) and not visited[i]:
                visited[i] = True
                route.append(words[i])
                dfs(words[i])
                route.pop()
                visited[i] = False
    
    dfs(begin)
    
    return answer