list_1=[]
for i in range(0,50):
    list_1.append(i+1)
a,b=input().split()
a=int(a)
b=int(b)
list_1=list_1[a:b]
for i in range(0,len(list_1)):
    print(list_1[i])

