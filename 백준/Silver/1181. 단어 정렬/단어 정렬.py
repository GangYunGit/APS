N = int(input())
words = set()
for i in range(N):
    word = input()
    words.add((word, len(word)))
words_list = list(words)
words_list.sort(key=lambda x: (x[1], x[0]))

for word in words_list:
    print(word[0], end="\n")