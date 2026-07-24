from collections import Counter

WINNING_COMBINATIONS = [ 
        (0,1,2), 
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6),
    ]

def gamestate(board):
    x_won = False
    o_won = False

    flatten_list = [cell for row in board for cell in row]
    for combination in WINNING_COMBINATIONS:
        if all(flatten_list[i] == "X" for i in combination):
            x_won = True
        if all(flatten_list[i] == "O" for i in combination):
            o_won = True

    counts = Counter(flatten_list)
    number_of_xs = counts["X"]
    number_of_os = counts["O"]
    number_of_spaces = counts[" "]
        
    if x_won and o_won:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if number_of_os > number_of_xs:
        raise ValueError("Wrong turn order: O started")
    if number_of_xs - number_of_os > 1:
        raise ValueError("Wrong turn order: X went twice")
    if x_won or o_won:
        return "win"   
    if number_of_spaces > 0:
        return "ongoing"
    return "draw"