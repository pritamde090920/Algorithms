def print_parenthesis(m,j,i):
    if j==i:
        print(chr(65+j),end="")
        return
    else:
        print("(",end="")
        print_parenthesis(m,m[j][i]-1,i)
        print_parenthesis(m,j,m[j][i])
        print(")",end="")
 
def matrix_chain_multiplication(p,n):
    m=[[0 for i in range(n)]
            for i in range (n)]
    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            m[i][j]=float('Inf')
            for k in range(i,j):
                q=(m[i][k]+m[k+1][j]+(p[i]*p[k+1]*p[j+1]));
                if q<m[i][j]:
                    m[i][j]=q
                    m[j][i]=k+1
    return m

arr=list(map(int,input("Enter the dimensions of the martices seperated by a space:").split()))
n=len(arr)-1
m=matrix_chain_multiplication(arr,n)
print("Minimum number of multiplications is :",m[0][n-1])
print("Placement of parenthesis for Optimal Parenthesization is : ",end="")
print_parenthesis(m,n-1,0)
