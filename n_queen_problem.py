result=[]

def is_safe(board,row,col):
    for i in range(col):
        if(board[row][i]):
            return False
    i=row
    j=col
    while i>=0 and j>=0:
        if(board[i][j]):
            return False
        i-=1
        j-=1
    i=row
    j=col
    while j>=0 and i<n:
        if(board[i][j]):
            return False
        i=i+1
        j=j-1
    return True

def solve_n_q_util(board,col):
    if (col==n):
        v=[]
        for i in board:
          for j in range(len(i)):
            if i[j]==1:
              v.append(j+1)
        result.append(v)
        return True
    res=False
    for i in range(n):
        if (is_safe(board,i,col)):
            board[i][col]=1
            res=solve_n_q_util(board,col+1) or res
            board[i][col]=0
    return res

def solve_n_q(n):
    result.clear()
    board=[[0 for j in range(n)]
             for i in range(n)]
    solve_n_q_util(board,0)
    result.sort()
    return result

n=int(input("Enter the no of queens to be placed:"))
res=solve_n_q(n)
print("The solutions for the",str(n)+"-queen problem is :",res)
sol=0
for i in res:
    print("\nSolution",sol+1)
    sol+=1
    for j in i:
        s=''
        for k in range(n):
            if k==(j-1):
                s+=' Q'
            else:
                s+=' -'
        print(s)
