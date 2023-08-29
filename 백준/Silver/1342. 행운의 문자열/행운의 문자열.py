def combinations():
    word_length = len(words)

    if len(pick) == word_length:
        new_word = "".join(pick)
        for i in range(word_length - 1):
            if pick[i] == pick[i + 1]:
                return

        if new_word not in lucky_string:
            lucky_string.add(new_word)
        return

    for i in range(word_length):
        if not used[i]:
            used[i] = True
            pick.append(words[i])
            combinations()
            pick.pop()
            used[i] = False


words = list(map(str, input()))
pick = []
used = [False for _ in range(len(words))]
lucky_string = set()
combinations()
print(len(lucky_string))