list_1=[]
for i in range(0,50):
    list_1.append(i+1)
a=int(input())
count=0
for i in range(0,50):
    if(list_1[i]%a==0 and list_1[i]!=a):
        count=count+1
print(count,end="")