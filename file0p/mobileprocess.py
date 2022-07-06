fread=open("mobile.txt")
# all_mobiles=[]
# for line in fread:
#     mobile=line.rstrip("\n").split(",")
#     all_mobiles.append(mobile)
# print(all_mobiles)

all_mobile=[mobile.rstrip("\n").split(",") for mobile in fread ]
print(all_mobile)

costly_mobile=max(all_mobile,key=lambda mob:int(mob[2]))
print(costly_mobile)

fivg_mobiles=[mob for mob in all_mobile if mob[3]=="5g"]
print(fivg_mobiles)

