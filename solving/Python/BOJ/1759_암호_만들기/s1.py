# BOJ_1759. 암호 만들기

def dfs_vowel(start, end, pick_consonant):
    if len(pick_vowel) == end:
        password = ''
        for char in sorted(pick_vowel + pick_consonant):
            password += char
        words.append(password)
        return

    for i in range(start, len(vowel)):
        pick_vowel.append(vowel[i])
        dfs_vowel(i + 1, end, pick_consonant)
        pick_vowel.pop()


def dfs_consonant(start, end):
    if len(pick_consonant) == end:
        dfs_vowel(0, L - end, pick_consonant)
        return

    for i in range(start, len(consonant)):
        pick_consonant.append(consonant[i])
        dfs_consonant(i + 1, end)
        pick_consonant.pop()


L, C = map(int, input().split())
word_list = sorted(list(input().split()))
vowel_char = {'a', 'e', 'i', 'o', 'u'}
vowel = []
consonant = []

for word in word_list:
    if word in vowel_char:
        vowel.append(word)
    else:
        consonant.append(word)

pick_vowel = []
pick_consonant = []
words = []
for i in range(1, len(vowel) + 1):
    if L - i >= 2:
        dfs_consonant(0, L - i)

print(*sorted(words), sep="\n")
