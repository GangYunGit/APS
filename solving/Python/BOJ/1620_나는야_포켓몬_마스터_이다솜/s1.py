# BOJ_1620. 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poketmon_dictionary = {i + 1: input().rstrip() for i in range(n)}
reverse_dictionary = dict()
for key, value in poketmon_dictionary.items():
    reverse_dictionary.setdefault(value, key)

for i in range(m):
    input_data = input().rstrip()
    if input_data.isdecimal():
        print(poketmon_dictionary[int(input_data)])
    else:
        print(reverse_dictionary[input_data])


