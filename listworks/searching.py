lst=[1,2,3,13,14,15,16,65]
element=159

flag=0
for num in lst:
    if element ==num:
        flag=1
        break
print("element found" if flag!=0 else "not found")
