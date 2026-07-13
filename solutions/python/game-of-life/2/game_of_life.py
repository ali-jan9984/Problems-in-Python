def tick(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    columns = len(matrix[0])
    g_matrix = [[0]*columns for _ in range(rows)]
    
    dr = (0,0,-1,1,-1,-1,1,1)
    dc = (1,-1,0,0,-1,1,-1,1)

    for i in range(rows):
        for j in range(columns):
            neighbors = [False] * 8
            count = 0
            for k in range(8):
                r_move = i + dr[k]
                c_move = j + dc[k]
                if (r_move > -1 and r_move < rows) and (c_move > -1 and c_move < columns):
                    if matrix[r_move][c_move]:
                        neighbors[k] = True
                        count+=1
            if matrix[i][j]:
                if (count == 2 or count == 3):
                    g_matrix[i][j] = 1
                else:
                    g_matrix[i][j] = 0
            else:
                if count == 3:
                    g_matrix[i][j] = 1
                else:
                    g_matrix[i][j] = 0
    return g_matrix        