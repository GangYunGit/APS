import sys
input = sys.stdin.readline

N = int(input())
words = set()
words_list = []
for i in range(N):
    word = input()
    words.add(word)
for i in words:
    words_list.append((len(i), i))
words_list.sort()

for word in words_list:
    print(word[1], end="")