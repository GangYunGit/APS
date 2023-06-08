def solution(record):
    user_id = []
    user_nickname = []
    result = []
    for info in record:
        info = info.split()
        if len(info) == 3:
            user_id.append(info[1])
            user_nickname.append(info[2])
    user_info = {user_id[_]: user_nickname[_] for _ in range(len(user_id))}

    for sentence in record:
        sentence = sentence.split()
        if sentence[0] == "Enter":
            result.append(f'{user_info[sentence[1]]}님이 들어왔습니다.')

        elif sentence[0] == "Leave":
            result.append(f'{user_info[sentence[1]]}님이 나갔습니다.')

    answer = result

    return answer