l=[]
l=[int(l) for l in input().split()]
final_list=[]
for num in l:
    if num not in final_list:
        final_list.append(num)
        
for i  in range(len(final_list)):
    if(final_list==len(final_list)-1):
        print(final_list[i],end="")
    else:
        print(final_list[i])
