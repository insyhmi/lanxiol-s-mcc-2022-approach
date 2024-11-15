import itertools
from itertools import chain

def card_shark (stack):
    p = list(itertools.permutations(stack))
    max_diff = -float('inf')
    for i in p:
        player = {
            1 : 0,
            2 : 0
        }
        all_cards = list(chain.from_iterable(i))
        for j in enumerate(all_cards):
            player[((j[0])%2) + 1] += j[1]
        if (player[1] - player[2]) > max_diff:
            max_diff = player[1] - player[2]
    return max_diff

#driver section
stack = [[4, 5], [6, 2, 3], [8], [1, 2, 5, 0]]

print (card_shark(stack))