numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]

p_count=0
z_count=0
n_count=0
for num in numbers:
    if num<0:
        n_count+=1
    elif num>0:
        p_count+=1
    elif num==0:
        z_count+=1
print(f"+ve count{p_count},-ve count{n_count},zero count{z_count}")

#pcount sum
#ncount sum

