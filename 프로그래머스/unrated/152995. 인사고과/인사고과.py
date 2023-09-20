def solution(scores):
    answer = 1
    wanho_score = scores[0]
    scores = scores[1:]
    scores.sort(key=lambda x: (-x[0], x[1]))
    prev_score = [-1, -1]
    for score in scores:
        if prev_score[0] > score[0] and prev_score[1] > score[1]:
            continue
        
        if wanho_score[0] < score[0] and wanho_score[1] < score[1]:
            answer = -1
            break
            
        if sum(score) > sum(wanho_score):
            answer += 1
        prev_score = score        
    
    return answer