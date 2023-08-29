def combinations(prev_word):
    word_length = len(words)

    if len(pick) == word_length:
        new_word = "".join(pick)
        if new_word not in lucky_string:
            lucky_string.add(new_word)
        return

    for i in range(word_length):
        if not used[i] and words[i] != prev_word:
            used[i] = True
            pick.append(words[i])
            combinations(words[i])
            pick.pop()
            used[i] = False


words = list(map(str, input()))
pick = []
used = [False for _ in range(len(words))]
lucky_string = set()
combinations("")
print(len(lucky_string))