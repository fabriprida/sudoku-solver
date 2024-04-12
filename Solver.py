import time

class Solver():
    def __init__(self, N) -> None:
        self.N = N

    def solve(self, sudoku):
        has_solution = self.has_solution(sudoku, 0, 0)
        if has_solution:
            print("SOLUCION:")
            self.print_sudoku(sudoku)
            print("\n")
        else: 
            print("NO EXISTE SOLUCION")
        return has_solution


    def has_solution(self, sudoku, i, j):
        if (i == self.N):
            return self.is_valid_solution(sudoku)

        sig_i, sig_j = self.sig(i, j)
        if (sudoku[i][j] == 0):
            solution = False
            for x in self.candidatos(sudoku, i, j):
                sudoku[i][j] = x 
                solution = self.has_solution(sudoku, sig_i, sig_j)
                if (solution):
                    return solution 
            sudoku[i][j] = 0
            return False 
        else: 
            return self.has_solution(sudoku, sig_i, sig_j)
        
    
    def candidatos(self, sudoku, i, j):
        fila = sudoku[i][0:max(0, j-1)]
        columna = [fila[j] for fila in sudoku][0:max(0, i-1)]
        return [x for x in range(1, self.N+1) if x not in fila and x not in columna]
        
        

            

    def print_sudoku(self, sudoku):
        for row in sudoku:
            print('|' + '|'.join(str(num) for num in row) + '|')


    def sig(self, i, j):
        if (j < self.N - 1):
            return (i, j+1)
        else: 
            return (i+1, 0)


    def is_valid_solution(self, sudoku):
        return (self.valid_rows(sudoku) and self.valid_columns(sudoku))
        

    def valid_rows(self, sudoku):
        expected = [i for i in range(1, self.N + 1)]

        for row in sudoku:
            if (sorted(row) != expected):
                return False 
            
        return True 


    def valid_columns(self, sudoku):
        expected = [i for i in range(1, self.N + 1)]
        columns = [[row[i] for row in sudoku] for i in range(self.N)] #REVISAR

        for col in columns:
            if (sorted(col) != expected):
                return False 
            
        return True


