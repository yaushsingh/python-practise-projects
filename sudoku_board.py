matrix = []

for i in range (4):
    print(f"Enter the elements separated with commas of {i+1} row")
    rows = [ int(x) for x in input().split(',')] #input.strip().split()works not .split().strip()
    matrix.append(rows)
for i in range(4):
    print(matrix[i])
print('your solved sudoku is ')

def checking(x,y,n):
    global matrix
    for i in range(4):
        if matrix[x][i] == n:
            return False
    for i in range(4):
        if matrix[i][y] == n:
            return False
    return True

def sudoku_solver():
    global matrix
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                for n in range(1,5):
                    if checking(i,j,n) == True:
                        matrix[i][j] = n
                        sudoku_solver(board)
                                    
                    return
    for a in range(4):
        print(matrix[a])
