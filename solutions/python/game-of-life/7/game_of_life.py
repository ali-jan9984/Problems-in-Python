def tick(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    columns = len(matrix[0])
    new_grid = [[0]*columns for _ in range(rows)]
    
    row_moves = (0,0,-1,1,-1,-1,1,1)
    col_moves = (1,-1,0,0,-1,1,-1,1)
    for i in range(rows):
        for j in range(columns):
            count = 0
            for k in range(8):
                r_move = i + row_moves[k]
                c_move = j + col_moves[k]
                if((r_move > -1 and r_move < rows) and (c_move > -1 and c_move < columns)):
                    if matrix[r_move][c_move]:
                        count+=1
            if count == 3:
                new_grid[i][j] = 1
            if count == 2 and matrix[i][j]:
                new_grid[i][j] = 1
    return new_grid        