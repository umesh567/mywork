# age=int(input("enter no1"))
#
# if (age<18):
#     raise Exception("not eligible for boosterdose")
# else:
#
#     print("eligible")

#raise error specific ayi user create cheyyunnathe ane   #throwing custom exception


no=(input("enter phone number"))

if(len(no)!=10):
    raise Exception ("phone no is not correct")
else:
    print("phone number is valid")