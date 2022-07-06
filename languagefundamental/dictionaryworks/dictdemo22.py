mobile={"mobile_name":"redmi",
        "ram":"6gb",
        "memory":"128gb",
        "price":45000
        }

print(mobile.get("mobile_name"))

#update band key::::::::::::::

#if "band" in mobile:
 #       mobile["band"]="5g"
#else:
 #       mobile["band"]="4g"
#print(mobile)


#one line method:::::::::::::::::::

mobile["band"]="5g" if "band" in mobile else "4g"
print(mobile)

#price update c_price-1000 if cur_price>40000 else c_price -500

if mobile["price"]>40000:
        mobile["price"]-=1000
else:
        mobile["price"]-=500
print(mobile)
