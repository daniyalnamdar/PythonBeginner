





def find_next_empty(puzzle):
    #find the next row, col not filled yet

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None #if no spaces in the puzzle left


def is_valid(puzzle, guess, row, col):
    # lest check the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #now the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #now the three by three grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True
    

def solve_sodoku(puzzle):
    #solve sodoku

    #first step is to choose somewhere on the board to start the guess

    row, col = find_next_empty(puzzle)

    #step 1.1 if there is nowhere left then we  
    if row is None:
        return True
    
    #step 2 if there is place to put number then make a guess
    for guess in range(1, 10):
        #step 3: check the validity
        if is_valid(puzzle, guess, row, col): 
            puzzle[row][col] = guess

            if solve_sodoku(puzzle):
                return True

        puzzle[row][col] = -1

# unsolveable puzzle
    return False      

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sodoku(example_board))
    print(example_board)
