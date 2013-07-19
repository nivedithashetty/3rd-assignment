c=[[0 for i in range(20)] for j in range(20)]
b=[[0 for i in range(20)] for j in range(20)]


def lcs(x,y):
    for i in range(1,m):
        c[i][0]=0
    for j in range(0,n):
        c[0][j]=0
    for i in range(0,m):
        for j in range(0,n):
            if x[i]==y[j]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]="@"
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]="^"
            else:
                c[i][j]=c[i][j-1]
                b[i][j]="<"


def printlcs(x,b,i,j):
    if i==-1 or j==-1:
        return
    if (b[i][j]=="@"):
        printlcs(x,b,i-1,j-1)
        print x[i]
        
       
    elif (b[i][j]=="^"):
        printlcs(x,b,i-1,j)
    elif (b[i][j]=="<"):
        printlcs(x,b,i,j-1)
        
x=raw_input("enter 1st string ")
y=raw_input("enter 2nd string ")
m=len(x)
n=len(y)
lcs(x,y)
print "the longest common sub sub sequence is:"
printlcs(x,b,m-1,n-1)



