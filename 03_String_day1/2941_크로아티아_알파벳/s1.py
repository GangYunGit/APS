# 2941_크로아티아_알파벳

how_many_croatia_alphabet = 0
croatia_alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'd-', 'lj', 'nj', 's=', 'z=']

my_croatia_word = input()

# 크로아티아 알파벳 개수를 먼저 카운트
for croatia_alphabet in croatia_alphabet_list:
    how_many_croatia_alphabet += my_croatia_word.count(croatia_alphabet)    # count메서드 사용
    # replace를 이용하여 아무 문자로 변경
    my_croatia_word = my_croatia_word.replace(croatia_alphabet, ' ')

# 나머지 알파벳 개수를 카운트
for alphabet in my_croatia_word:
    if 65 <= ord(alphabet) <= 90 or 97 <= ord(alphabet) <= 122:
        how_many_croatia_alphabet += 1

print(how_many_croatia_alphabet)

