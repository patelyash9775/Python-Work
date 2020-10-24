import math

n=int(input())
d={}
d['RIGHT']=0
d['LEFT']=0
d['UP']=0
d['DOWN']=0
for i in range(n):
    dirc,move=input().split()
    move=int(move)
    d[dirc]+=move
x=d['RIGHT']-d['LEFT']
y=d['UP']-d['DOWN']

distance=math.sqrt((x*x)+(y*y))
print(round(distance),end="")
    
