from collections import deque
from itertools import islice

def play_game(decks: tuple[deque, deque]) -> int:
    positions = set()
    initial_position = (tuple(decks[0]), tuple(decks[1]))
    if initial_position in games:
        return games[initial_position]

    while decks[0] and decks[1]:
        position = (tuple(decks[0]), tuple(decks[1]))
        if position in positions:
            games[initial_position] = 0
            return 0
        else:
            positions.add(position)

        card1 = decks[0].popleft()
        card2 = decks[1].popleft()
        if card1 <= len(decks[0]) and card2 <= len(decks[1]):
            new_decks = (deque(islice(decks[0], 0, card1)), deque(islice(decks[1], 0, card2)))
            winner = play_game(new_decks)
        elif card1 > card2:
            winner = 0
        else:
            winner = 1
        decks[0].extend([card1, card2]) if winner == 0 else decks[1].extend([card2, card1])

    winner = 0 if decks[0] else 1
    games[initial_position] = winner
    return winner

with open('input') as f:
    decks = [x.split('\n')[1:] for x in f.read().split('\n\n')]

decks = tuple([deque([int(x) for x in deck]) for deck in decks])
games = {}
winner = play_game(decks)
total = sum((x*(i+1) for i, x in enumerate(reversed(decks[winner]))))
print(total)