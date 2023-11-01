import sys
input = sys.stdin.readline


def time(get_time):
    hour, minute = map(int, get_time.split(':'))
    return 60 * hour + minute


start_time, end_time, end_streaming_time = map(time, input().split())
attendance = set()
count = 0
while True:
    try:
        chatting = input()
        chat_time, nickname = chatting.split()
        if time(chat_time) <= start_time:
            attendance.add(nickname)
        elif end_time <= time(chat_time) <= end_streaming_time and nickname in attendance:
            attendance.remove(nickname)
            count += 1
    except:
        break
print(count)