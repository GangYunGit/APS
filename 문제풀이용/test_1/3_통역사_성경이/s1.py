# 7675_통역사_성경이

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    talk = input()
    sentence_list = []
    sentence_divide = ''
    result_list = []

    for word in talk:
        sentence_divide += word
        if word == "." or word == "?" or word == "!":
            sentence_divide = sentence_divide.lstrip()
            sentence_divide = sentence_divide[:len(sentence_divide) - 1:]
            sentence_list.append(sentence_divide)
            sentence_divide = ''

    name_list = []
    for sentence in sentence_list:
        result = 0
        name_list = sentence.split()
        for name in name_list:
            find_name = 0
            for i in range(len(name)):
                if i == 0 and (name[i].islower() or name[i].isdigit()):
                    find_name += 1
                    break
                if i > 0 and (name[i].isupper() or name[i].isdigit()):
                    find_name += 1
                    break
            if find_name == 0:
                result += 1
        result_list.append(result)
    print(f'#{test_case}', end=' ')
    print(*result_list)
