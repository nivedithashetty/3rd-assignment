m=[[0 for i in range(10)] for j in range(10)]
s=[[0 for i in range(10)] for j in range(10)]
   
def MatrixChainOrder(p,n):
    for i in range(1,n+1):
        m[i][i]=0
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            m[i][j]=99999999
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j];
                if (q<m[i][j]):
                    m[i][j]=q
                    s[i][j]=k

def print_paren(s,i,j):
    if i==j:
        print "A"
    else:
        print"("
        print_paren(s,i,s[i][j])
        print_paren(s,s[i][j]+1,j)
        print")"
    


 
p=[5,10,3,12,5,50,6]
n=len(p)-1
MatrixChainOrder(p, n)

print_paren(s,1,n)
