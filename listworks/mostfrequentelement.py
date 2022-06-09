lst1=[10,11,11,12,13,14,14,14,14,14]

dup_lst=[]
for i in range(0,len(lst1)):
    for j in range((i+1),len(lst1)):
        if lst1[i]==lst1[j]:
            dup_lst.append(lst1[i])
print(dup_lst)
