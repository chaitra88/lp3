def print_board(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()
    print()

def isSafe(board,row,col,n):
    for i in range(n):
        if board[i][col]==1 and i!=row:
            return False
    for i in range(n):
        for j in range(n):
            if board[i][j]==1 and (abs(row-i))==abs(col-j):
                return False
    return True
            
def solve(board,row,n):
    if row==n:
        print_board(board,n)
        return
    if 1 in board[row]:
        solve(board,row+1,n)
        return
    for col in range(n):
        if isSafe(board,row,col,n):
            board[row][col]=1
            solve(board,row+1,n)
            board[row][col]=0
    return board


def n_queens(f_row,f_col,n):
    board=[[0 for _ in range(n)]for _ in range(n)]
    board[f_row][f_col]=1
    solve(board,0,n)

n=int(input("entrer board size: "))
fr=int(input("enter first row (0--->n-1)"))
fc=int(input("enter first col (0--->n-1)"))
n_queens(fr,fc,n)