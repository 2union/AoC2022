from enum import Enum

class Move(Enum):
    A = 1 # rock
    B = 2 # paper
    C = 3 # scissors
    X = 1
    Y = 2
    Z = 3


def check_points(p1, p2):
    if Move[p1].value == Move[p2].value:
        return 3, 3
    match p1:
        case 'A':
            if p2 == 'Y':
                return 0, 6
            else:
                return 6, 0
        case 'B':
            if p2 == 'Z':
                return 0, 6
            else:
                return 6, 0
        case 'C':
            if p2 == 'X':
                return 0, 6
            else:
                return 6, 0

player_one_score = 0
player_two_score = 0

with open('input') as f:
    for l in f:
        p_one_move, p_two_move = l.strip().split(' ')
        p_one_goal, p_two_goal = check_points(p_one_move, p_two_move)
        print(p_one_move, p_two_move, p_one_goal, p_two_goal)
        player_one_score += p_one_goal + Move[p_one_move].value
        player_two_score += p_two_goal + Move[p_two_move].value

print(player_one_score)
print(player_two_score)
