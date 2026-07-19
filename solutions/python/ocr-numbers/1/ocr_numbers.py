def convert(input_grid):
    lookup_table = {
        (" _ ","| |","|_|","   "):'0',
        ("   ","  |","  |","   "):'1',
        (" _ "," _|","|_ ","   "):'2',
        (" _ "," _|"," _|","   "):'3',
        ("   ","|_|","  |","   "):'4',
        (" _ ","|_ "," _|","   "):'5',
        (" _ ","|_ ","|_|","   "):'6',
        (" _ ","  |","  |","   "):'7',
        (" _ ","|_|","|_|","   "):'8',
        (" _ ","|_|"," _|","   "):'9'
    }
    if (len(input_grid) % 4 != 0):
        raise ValueError("Number of input lines is not a multiple of four")
    if(len(input_grid[0]) % 3 != 0):
        raise ValueError("Number of input columns is not a multiple of three")

    all_lines_processed = []

    for r in range(0,len(input_grid),4):
        current_row_strip = input_grid[r: r + 4]
        line_digits = ""
        num_cols = len(current_row_strip[0])
        
        for c in range(0,num_cols,3):
            digit_row = (
                current_row_strip[0][c:c+3],
                current_row_strip[1][c:c+3],
                current_row_strip[2][c:c+3],
                current_row_strip[3][c:c+3]
            )
            if digit_row in lookup_table:
                line_digits += lookup_table[digit_row]
            else:
                line_digits += "?"
        all_lines_processed.append(line_digits)
    return ",".join(all_lines_processed)