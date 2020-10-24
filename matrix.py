r,c=input().split()
r=int(r)
c=int(c)
matrix=[]
l=[]
count=0
for i in range(r):
    for j in range(c):
        l.append(0)
    matrix.append(l)
for i in range(r):
    for j in range(c):
        count=count+1
        matrix[i][j]=count
        print(matrix[i][j],end=" ")
    if(count!=(r*c)):
        print()
    else:
        print(end="")

