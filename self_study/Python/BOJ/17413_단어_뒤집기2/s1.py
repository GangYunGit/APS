# BOJ_17413. 단어 뒤집기2

my_string = input()
is_tag_string = False
is_original_string = False
tag_string = ''
reverse_string = ''

for i in range(len(my_string)):
    if i == 0:
        if my_string[i] == '<' or my_string[i] == '>':
            is_original_string = False
            is_tag_string = True
        else:
            is_original_string = True
            is_tag_string = False

    if my_string[i] == '<':
        is_tag_string = True
        is_original_string = False
        print(reverse_string[::-1], end='')
        reverse_string = ''
        tag_string += my_string[i]

    elif my_string[i] == '>':
        is_tag_string = False
        is_original_string = True
        tag_string += my_string[i]
        print(tag_string, end='')
        tag_string = ''

    elif i == len(my_string) - 1:
        reverse_string += my_string[i]
        print(reverse_string[::-1])

    elif is_tag_string:
        tag_string += my_string[i]

    elif is_original_string:
        if my_string[i] == ' ':
            print(reverse_string[::-1], end=' ')
            reverse_string = ''
        else:
            reverse_string += my_string[i]
