how_many_croatia_alphabet = 0
croatia_alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'd-', 'lj', 'nj', 's=', 'z=']

my_croatia_word = input()

for croatia_alphabet in croatia_alphabet_list:
    how_many_croatia_alphabet += my_croatia_word.count(croatia_alphabet)
    my_croatia_word = my_croatia_word.replace(croatia_alphabet, ' ')

for alphabet in my_croatia_word:
    if 65 <= ord(alphabet) <= 90 or 97 <= ord(alphabet) <= 122:
        how_many_croatia_alphabet += 1

print(how_many_croatia_alphabet)