import collections

with open('input') as f:
    decks = [x.split('\n')[1:] for x in f.read().split('\n\n')]

deck1 = collections.deque([int(x) for x in decks[0]])
deck2 = collections.deque([int(x) for x in decks[1]])

while deck1 and deck2:
    card1 = deck1.popleft()
    card2 = deck2.popleft()
    if card1 > card2:
        deck1.extend([card1, card2])
    elif card2 > card1:
        deck2.extend([card2, card1])

deck1.extend(deck2)
total = sum((x*(i+1) for i, x in enumerate(reversed(deck1))))

print(total)