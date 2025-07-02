'''
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''
def isValidSudoku(board) -> bool:
    # no dupe in row or col
    cols = [set() for i in range(9)]
    for row in range(9):
        seen = set()
        for col in range(9):
            num = board[row][col]
            
            if num in seen: # if dupe in row
                return False
            elif num != ".":
                seen.add(num)

            if num in cols[col]: # if dupe in col
                return False
            elif num != ".":
                cols[col].add(num)


    # no dupe in square
    for box_row in range(3):
        for box_col in range(3):
            seen = set()
            
            for i in range(3):
                for j in range(3):
                    num = board[i + box_row * 3][j + box_col * 3]
                    if num in seen:
                        return False
                    elif num != ".":
                        seen.add(num)
    return True