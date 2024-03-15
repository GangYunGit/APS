word = input()
new_word = ""
idx = 0
while True:
    if idx > len(word) - 1:
        break
    new_word += word[idx]
    if word[idx] in {'a', 'e', 'i', 'o', 'u'}:
        idx += 3
    else:
        idx += 1
print(new_word)