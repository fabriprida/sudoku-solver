def solver(sudoku, i, j):

    if (i == 9):
        if (check_if_valid(sudoku)):
            print("SOLUTION:")
            print_sudoku(sudoku)
            print("------------------------")
    else:
        if (sudoku[i][j] == 0):
            for x in range(1,10):
                sudoku[i][j] = x 
                sig_i, sig_j = sig(i, j)
                solver(sudoku, sig_i, sig_j)
                sudoku[i][j] = 0
        else: 
            sig_i, sig_j = sig(i, j)
            solver(sudoku, sig_i, sig_j)
        

def print_sudoku(sudoku):
    for row in sudoku:
        print('|' + '|'.join(str(num) for num in row) + '|')


def sig(i, j):
    if (j < 8):
        return i, j+1
    else: 
        return i+1, 0

def check_if_valid(sudoku):
    return (check_if_rows_valid(sudoku) and check_if_columns_valid(sudoku))
    

def check_if_rows_valid(sudoku):
    expected = [i for i in range(1, 10)]

    for row in sudoku:
        if (sorted(row) != expected):
            return False 
        
    return True 


def check_if_columns_valid(sudoku):
    expected = [i for i in range(1, 10)]
    columns = [[row[i] for row in sudoku] for i in range(9)] #REVISAR

    for col in columns:
        if (sorted(col) != expected):
            return False 
        
    return True


def create_sudoku():
    #sudoku = [[0] * 9 for i in range(9)]
    sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

solver(sudoku, 0, 0)

valid_sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

if (check_if_valid(valid_sudoku)):
    print("yes")
else: 
    print("no")