def gamestate(board):
    number_of_xs = 0;
    number_of_os = 0;
    number_of_spaces = 0;

    x_positions = [0] * 9
    o_positions = [0] * 9

    winning_combinations = [
        [0,1,2], 
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6],
    ]
    x_won = False
    o_won = False

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                number_of_xs+=1
                x_positions[row * 3 + col] = 1
            elif board[row][col] == "O":
                number_of_os+=1
                o_positions[row * 3 + col] = 1
            else:
                number_of_spaces+=1
                
    for combination in winning_combinations: 
        if x_positions[combination[0]] and x_positions[combination[1]] and x_positions[combination[2]]:
            x_won = True
        if o_positions[combination[0]] and o_positions[combination[1]] and o_positions[combination[2]]:
            o_won = True
    
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
    else:
        return "draw"