n = int(input())
meeting_list = [list(map(int, input().split())) for _ in range(n)]
meeting_list.sort()
room_end_time_list = []
for start, end in meeting_list:
    if not room_end_time_list:
        room_end_time_list.append(end)
    else:
        for i in range(len(room_end_time_list)):
            if room_end_time_list[i] <= start:
                room_end_time_list[i] = end
                break
        else:
            room_end_time_list.append(end)

print(len(room_end_time_list))