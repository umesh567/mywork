dic={"k1":10,"k2":"hello","k3":"True"}

print(dic.get("k4"))

for k,v in dic.items():
    print(k,v)


for v in dic.values():
    print(v)



dic.pop("k3")
print(dic)
