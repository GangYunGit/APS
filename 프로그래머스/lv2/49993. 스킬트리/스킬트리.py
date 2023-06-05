def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        next_skill_index = 0                # 스킬 트리의 첫 번째 스킬부터 검사하기 위해 인덱스 지정

        for custom_skill in skill_tree:     # 해당 스킬트리의 스킬을 하나씩 검사
            if custom_skill in skill:       # 스킬을 검사하면서 선행 스킬순서에 포함되어있고
                if next_skill_index != skill.index(custom_skill):   # 검사한 스킬의 순서가 스킬트리의 순서와 맞지 않으면 break
                    break
                else:                                               # 순서가 맞으면 다음 스킬을 확인하기 위해 index + 1
                    next_skill_index += 1                           
                    
        else:                               # for else문 => for문을 돌면서 break문에 의해 종료되지 않았다면 else문으로 오게 됨
            answer += 1    
                    
    return answer