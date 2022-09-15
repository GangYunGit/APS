# BOJ_2161_카드

N = int(input())
my_deck = [_ + 1 for _ in range(N)]

while len(my_deck) != 1:
    remove = my_deck.pop(0)
    my_deck.append(my_deck.pop(0))
    print(remove, end=' ')

print(my_deck[0])
