import Solver


easy_4x4_sudoku = [
    [0, 2, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 4],
    [3, 0, 0, 0]
]


moderate_4x4_sudoku = [
    [0, 0, 0, 2],
    [0, 0, 3, 0],
    [0, 0, 0, 0],
    [2, 0, 0, 0]
]


difficult_4x4_sudoku = [
    [0, 0, 3, 0],
    [0, 0, 0, 2],
    [0, 0, 0, 0],
    [2, 0, 0, 0]
]



solver = Solver.Solver(4)
solver.solve(difficult_4x4_sudoku)


