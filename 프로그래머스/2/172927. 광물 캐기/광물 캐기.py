def solution(picks, minerals):
    answer = 0
    
    mineral_info = []
    for start_idx in range(0, len(minerals), 5):
        temp = []
        for i in range(5):
            if start_idx + i > len(minerals) - 1:
                break
            temp.append(minerals[start_idx + i])
        mineral_info.append(temp)
    
    fatigue_info = []
    for group in mineral_info:
        if len(fatigue_info) == sum(picks):
            break
        temp_fatigue = [0, 0, 0]    # 다이아 곡괭이, 철 곡괭이, 돌 곡괭이
        for i in range(len(group)):
            if group[i] == 'diamond':
                temp_fatigue[0] += 1
                temp_fatigue[1] += 5
                temp_fatigue[2] += 25
            elif group[i] == 'iron':
                temp_fatigue[0] += 1
                temp_fatigue[1] += 1
                temp_fatigue[2] += 5
            else:
                temp_fatigue[0] += 1
                temp_fatigue[1] += 1
                temp_fatigue[2] += 1
        fatigue_info.append(temp_fatigue)
    
    fatigue_info.sort(key=lambda x: -x[2])
    for fatigue in fatigue_info:
        for i in range(3):
            if picks[i] > 0:
                print(i)
                answer += fatigue[i]
                picks[i] -= 1
                break            
    
    return answer