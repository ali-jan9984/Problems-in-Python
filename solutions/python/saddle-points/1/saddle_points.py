def saddle_points(matrix):
    if not matrix:
        return []
        
    rows = len(matrix)
    columns = len(matrix[0])

    if any(len(row) != columns for row in matrix):
        raise ValueError("irregular matrix")

    max_in_rows = [0] * rows
    min_in_cols  = [0] * columns

    points = []  

    for i in range(rows):
        r_max = matrix[i][0]
        for j in range(columns):
            if r_max < matrix[i][j]:
                r_max = matrix[i][j]
        max_in_rows[i] = r_max 

    for j in range(columns):
        c_min = matrix[0][j]
        for i in range(rows):
            if c_min > matrix[i][j]:
                c_min = matrix[i][j]
        min_in_cols[j] = c_min

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == max_in_rows[i] and matrix[i][j] == min_in_cols[j]:
                points.append({"row": i + 1, "column": j + 1})
    
    return points