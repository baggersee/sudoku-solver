def empty_square(sudoku):
    # returns the coordinates of every square with 0 (empty)
    # if there are no empty squares, returns 'None,None'
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                return r,c
            
    return None,None

def is_solved(sudoku):
    # checks if the sudoku is already solved
    # it will be solved when no empty square remains and will return 'True'
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] ==0:
                return False 
    return True

def is_valid(sudoku,row,col,guess):
    # checks if a guess in the coordiantes (row,col) in 'sudoku' can fit
    # checking the rows
    if guess in sudoku[row]:
        return False
    
    #checking the columns
    columns = []
    for j in range(9):
        columns.append(sudoku[j][col])
        
    if guess in columns:
        return False
        
    # submatrix 3x3
    sub_matrix = []
    r = row//3 # 0, 1 or 2
    c = col//3
    for i in range(3*r,3*r+3):
        for j in range(3*c,3*c+3):
            sub_matrix.append(sudoku[i][j])
    #print(sub_matrix)        
            
    if guess in sub_matrix:
        return False
    
    # if it gets here, is because its valid
    return True


def sudoku_solver(sudoku):
    # main function that solves the sudoku
    # sudoku is a list of lists
    # using recursion until we get an unsolvable situation and then we trace back
    
    # we get the first empty square
    row,col = empty_square(sudoku)
    
    if row is None:
        return True # all the squares are filled and we are done
    
    else:
        
        for guess in range(1,10):
            # we choose a guess and we see if its valid
            if is_valid(sudoku,row,col,guess):
                # if its valid, we subsitute it
                sudoku[row][col] = guess
                if sudoku_solver(sudoku): # it runs 'sudoku_solver' until it reaches an unsolvable sudoku or a solved sudoku
                    return sudoku
                
            sudoku[row][col] = 0
        return False