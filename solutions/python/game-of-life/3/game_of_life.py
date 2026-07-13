def tick(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    columns = len(matrix[0])
    new_matrix = [[0]*columns for _ in range(rows)]
    
    row_moves = (0,0,-1,1,-1,-1,1,1)
    col_moves = (1,-1,0,0,-1,1,-1,1)

    for i in range(rows):
        for j in range(columns):
            neighbors = [False] * 8
            count = 0
            for k in range(8):
                r_move = i + row_moves[k]
                c_move = j + col_moves[k]
                if (r_move > -1 and r_move < rows) and (c_move > -1 and c_move < columns):
                    if matrix[r_move][c_move]:
                        neighbors[k] = True
                        count+=1
            if matrix[i][j]:
                if (count == 2 or count == 3):
                    new_matrix[i][j] = 1
                else:
                    new_matrix[i][j] = 0
            else:
                if count == 3:
                    new_matrix[i][j] = 1
                else:
                    new_matrix[i][j] = 0
    return new_matrix        