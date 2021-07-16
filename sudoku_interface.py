from tkinter import *
from sudoku_functions import empty_square,is_solved,is_valid,sudoku_solver

root = Tk()
root.title('Sudoku solver!')

# blank matrix (list of lists)
matrix = []
for i in range(9):
    matrix.append([])
    for j in range(9):
        matrix[i].append(0)
              
# generating the squares of the sudoku 
for i in range(9):
    for j in range(9):
        e = Entry(root,width=5,borderwidth=2)
        e.grid(row=i, column=j, columnspan=1, padx=2, pady=2)
        
squares_list = []
for i in range(9):
    squares_list.append([])
    for j in range(9):
        e = Entry(root,width=5,borderwidth=2)
        e.grid(row=i, column=j, columnspan=1, padx=2, pady=2)
        squares_list[i].append(e)
        
# import values functions
def solve():
    for i in range(9):
        for j in range(9):
            s = squares_list[i][j]
            number = s.get()
            if number == '':
                number = 0
                
            global matrix
            matrix[i][j] = int(number)
    global solution
    solution = sudoku_solver(matrix)
    write_solution()
    return

def write_solution():
    for i in range(9):
        for j in range(9):
            s = squares_list[i][j]
            num = solution[i][j]
            s.delete(0,END)
            s.insert(0,num)
    return
      
# generating the solving button
solving_button = Button(root, text="Solve me",padx=35,pady=2,borderwidth=8,command=  lambda:solve())
solving_button.grid(row=10,column=2,columnspan=4)

root.mainloop()
