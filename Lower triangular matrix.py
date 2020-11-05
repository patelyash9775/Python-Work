n=int(input())
l=[]
for i in range(n):
    row=list(map(int,input().split()))
    l.append(row)
    
for i in range(n):
    for j in range(n):
        if(i<j):
            l[i][j]=0
        if(j==n-1):
            print(l[i][j],end="")
        else:
            print(l[i][j],end=" ")
    if(i==n-1):
        print(end="")
    else:
        print()
    
