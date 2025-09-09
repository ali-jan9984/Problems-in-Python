class Queen:
    def __init__(self, row, column):
        #validate row
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")

        #validate column
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        #initialize the row and column for an object 
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        #check if queen is at the same row and column
        if another_queen.row == self.row and another_queen.column == self.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        same_row = another_queen.row == self.row
        same_column = another_queen.column == self.column
        same_diagnol = (abs(another_queen.row - self.row)) == (abs(another_queen.column - self.column))
        
        return same_row or same_column or same_diagnol