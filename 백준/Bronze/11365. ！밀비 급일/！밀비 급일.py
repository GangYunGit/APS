while True:
    line = input()
    if line == 'END':
        break
    for i in range(len(line) - 1, -1, -1):
        print(line[i], end="")
    print()