def find_maxvalue(dummy):
    for j in range(1,n+1):
        q[1][j]=c[1][j]
    for y in range(1,n+1):
        q[y][0]=0
        q[y][n+1]=0
    for i in range(2,n+1):
        for j in range(1,n+1):
            m=max(q[i-1][j-1],q[i-1][j],q[i-1][j+1])
            q[i][j]=m+c[i][j]
            if m==q[i-1][j-1]:
                p[i][j]=-1
            elif m==q[i-1][j]:
                p[i][j]=0
            else:
                p[i][j]=1


def display(i,j):
    print j
    print("^")
    if i==2:
        print(j+p[i][j])
    else:
        display(i-1,j+p[i][j])


def computeShortestPath(dummy):
    find_maxvalue(0)
    maxIndex=1
    mx=q[n][1]
    for i in range(2,n+1):
        if q[n][i]>mx:
            maxIndex=i
            mx=q[n][i]
    print " "
    display(n,maxIndex)
    print "optimal path starts from here "


n=5
c=[[0,0,0,0,0,0,0],[0,9,6,7,8,5,0],[0,5,9,8,7,8,0],[0,8,4,3,9,1,0],[0,6,9,7,1,9,0],[0,5,8,6,15,5,0]]
q=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
p=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
computeShortestPath(0)
