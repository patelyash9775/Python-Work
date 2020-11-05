import turtle
from random import randint

turtle.bgcolor('black')
seurat=turtle.Turtle()

width=5
height=7

dot_distance=25

seurat.penup()
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey"]
seurat.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0
    
    """
    k = index of starting row
    l = index of starting column
    """
    col=randint(0,9)
    seurat.color(list_color[col])
    while(k<=m and l<=n):
        
        if(f==1):
            seurat.right(90)
            
        #printing the first row from the remaining wsro
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i],end=" ")
            
        k+=1
        f=1
        
        seurat.right(90)
        col=randint(0,9)
        seurat.color(list_color[col])
        #printing the last column from the remaining coulmn 
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=" ")
            
        n-=1
        seurat.right(90)
        col=randint(0,9)
        seurat.color(list_color[col])
        if(k<m):
            #printing the last row for remaining row
            for i in range(n-1,(l-1),-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            
            m-=1
        seurat.right(90)
        col=randint(0,9)
        seurat.color(list_color[col])
        if(l<n):
            #printing the first column from the remaining column
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l],end=" ")
                
            l+=1
            
            

spiral(20,20)
turtle.done()