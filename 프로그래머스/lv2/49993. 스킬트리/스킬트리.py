def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        next_skill_index = 0
        for custom_skill in skill_tree:
            if custom_skill in skill:
                if next_skill_index != skill.index(custom_skill):
                    next_skill_index = -1
                    break
                else:
                    next_skill_index += 1
        if next_skill_index >= 0:
            answer += 1
            
    return answer