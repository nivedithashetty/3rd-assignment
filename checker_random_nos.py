import random
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



c=[[0 for i in range(15)] for j in range(15)]
q=[[0 for i in range(15)] for j in range(15)]
p=[[0 for i in range(15)] for j in range(15)]

n=int(raw_input("enter the size of the checker board"))
numbers=[1,2,3,4,5,6,7,8,9]
for i in range(1,n+1):
    for j in range(1,n+1):
        c[i][j]=random.choice(numbers)

print"entered board costs are as follows:"
for i in range(1,n+1):
    for j in range(1,n+1):
        print c[i][j]
    print " "
print " "
    

computeShortestPath(0)
