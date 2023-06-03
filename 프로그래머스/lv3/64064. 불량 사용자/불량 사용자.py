def id_checker(user_id, banned_id):
    user_id_length = len(user_id)
    banned_id_length = len(banned_id)
    if user_id_length != banned_id_length:
        return False
    
    for i in range(user_id_length):
        if banned_id[i] == "*":
            continue
        if user_id[i] != banned_id[i]:
            return False
    
    return True

def dfs(user_id, banned_id, choice, used):
    global result
    if len(choice) == len(banned_id):
        same_id_checked = True
        for i in range(len(choice)):
            if id_checker(choice[i], banned_id[i]):
                continue
            else:
                same_id_checked = False
                break
                
        if same_id_checked:
            temp = sorted(choice[:])
            if temp not in result:
                result.append(temp)
        
        return 
    
    for i in range(len(user_id)):
        if not used[i]:
            used[i] = True
            choice.append(user_id[i])
            dfs(user_id, banned_id, choice, used)
            used[i] = False
            choice.pop()
        

def solution(user_id, banned_id):
    global result
    choice = []
    used = [False for _ in range(len(user_id))]
    result = []
    dfs(user_id, banned_id, choice, used)
    
    return len(result)