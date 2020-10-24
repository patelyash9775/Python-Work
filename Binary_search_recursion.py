
def binary_search(l,x,start,end):
    #Base case: 1 element
    if(start==end):
        if(l[start]==x):
            return(start)
        else:
            return(-1)
    else:
        #Divide the array into half
        mid=int((start+end)/2)
        if(l[mid]==x):
            return(mid)
        elif(l[mid]>x):
            #left half
            return(binary_search(l, x, start, mid-1))
        else:
            #right half
            return(binary_search(l, x, mid+1, end))
        
        
l=[20,30,40,50,65,90]
x=int(input("Enter search an element :- "))
index=binary_search(l, x, 0, len(l)-1)
if(index==-1):
    print(x,' 45is not found')
else:
    print(x,' is found at position ',index+1)