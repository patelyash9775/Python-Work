
r=int(input())
m=r
n=r
a=[]
for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)
    
def traverse(m,n,a):
    r=0
    c=0
    b=[]
    while(r<=m and c<=n):
        
        for i in range(r,m):
            b.append(a[i][c])
              
        c+=1
        
        for i in range(c,n):
            b.append(a[m-1][i])
            
        m-=1
        
        if(c<n):
            for i in range(m-1,(r-1),-1):
                b.append(a[i][n-1])
                
        n-=1
        
        if(r<m):
            for i in range(n-1,c-1,-1):
                b.append(a[r][i])
                
        r+=1
        
    for i in range(0,len(b)):
        if(i==(len(b)-1)):
            print(b[i],end="")
        else:
            print(b[i],end=" ")
        
        
traverse(m, n, a)