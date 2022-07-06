#try = block doubtful code
#except = block handling code
#raise  = key word custom error throw
#finally = block clean up processing

num1=int(input("enter no 1"))
num2=int(input("enter no 2 "))

try:
    res=num1/num2    # ee line il error varan chance unde divisible by 0 koduthal error varum athe konde ane try molil use chythe
    print(f"result{res}")
except Exception as e: #ah error except ayi bakki thazhe ullthe print akan ane except use chythekkunnathe
    print(e)

finally:  #vere line error ayalum ee thazhe ulla line print akum athine finally use cheyyam

     print("db transaction")
     print("file operation")

