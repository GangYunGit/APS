n = int(input())
word_list = [input() for _ in range(n)]
number = [_ for _ in range(10)]
word_count = []
word_value = [0 for _ in range(10)]
for word in word_list:
    for alphabet in word:
        if alphabet not in word_count:
            word_count.append(alphabet)

for word in word_list:
    for i in range(len(word)):
        for j in range(len(word_count)):
            if word[i] == word_count[j]:
                word_value[j] += 10 ** (len(word) - i - 1)
word_value.sort()

for i in range(10):
    word_value[i] *= i
print(sum(word_value))