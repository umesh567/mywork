lst1=[10,11,12,13,14]
lst2=[11,14,15,16,17]
dup_lis=list()

for num in lst1:
    if num in lst2:
        dup_lis.append(num)
print(dup_lis)



