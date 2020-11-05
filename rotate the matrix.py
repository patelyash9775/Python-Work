
r=int(input())
m=r
n=r
a=[]
for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)

def traversing(a):
    
    top=0
    bottom=len(a)-1
    
    left=0
    right=len(a[0])-1
    
    while(left<right and top<bottom):
        
        p = a[top+1][left]
        
        for i in range(left,right+1):
            c=a[top][i]
            a[top][i]=p
            p=c
            
        top+=1
        
        for i in range(top,bottom+1):
            c=a[i][right]
            a[i][right]=p
            p=c
            
        right-=1
        
        for i in range(right,left-1,-1):
            c=a[bottom][i]
            a[bottom][i]=p
            p=c
            
        bottom-=1
        
        for i in range(bottom,top-1,-1):
            c=a[i][left]
            a[i][left]=p
            p=c
            
        left+=1
        
    return(a)


list=traversing(a)
print(len(list))
for i in range(0,m):
    for j in range(0,n):
        if(j==n-1):
            print(list[i][j],end="")
        else:
            print(list[i][j],end=" ")
    if(i==m-1):
        print(end="")
    else:
        print()           
          
