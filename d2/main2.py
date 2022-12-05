from enum import Enum

class Move(Enum):
    A = 1 # rock
    B = 2 # paper
    C = 3 # scissors

def win_lose(figure):
    if figure == 'A':
        return 'B', 'C'
    if figure == 'B':
        return 'C', 'A'
    if figure == 'C':
        return 'A', 'B'

player_one_score = 0
player_two_score = 0

with open('input') as f:
    for l in f:
        p_one_move, result = l.strip().split(' ')
        win_fig, lose_fig = win_lose(p_one_move)
        print(p_one_move, win_fig, lose_fig)
        if result == 'X':
            player_two_score += 0 + Move[lose_fig].value
            player_one_score += 6 + Move[p_one_move].value
        if result == 'Y':
            player_two_score += 3 + Move[p_one_move].value
            player_one_score += 3 + Move[p_one_move].value
        if result == 'Z':
            player_two_score += 6 + Move[win_fig].value
            player_one_score += 0 + Move[p_one_move].value

print(player_one_score)
print(player_two_score)
