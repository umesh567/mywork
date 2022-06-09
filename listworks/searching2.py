lst=[111,222,333,444,555]
element = 445
flag=0
for i in range (0,len(lst)):
    if element==lst[i]:
        flag=1
        break
print("element found "if flag!=0 else "element not found")

print(dir(list)) #method list cheyyan use cheyyunna method