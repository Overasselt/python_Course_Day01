import random

suits = ['clubs', 'diamonds', 'hearts', 'spades']

ranks = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')

cards = [f'{r} of {s}' for r in ranks for s in suits]
#voorheen werd dit zo gedaan
# cards = ['%s of %s' % (r,s) for r in ranks for s in suits]

random.shuffle(cards)

hand = [cards.pop() for _ in range(5)]

print(hand)