num1=10
num2=30
num3=60
if(num1>num2)and(num1>num3):
    if num2>num3:
        print(f"{num2} is second largest number")
    else:
        print(f"{num3} is second largest number")
elif(num2>num1)and(num2>num3):
    if num1>num3:
        print(f"{num1} is second largest number")
    else:
        print(f"{num3} is second largest number")
elif(num3>num1)and(num3>num2):
    if num1>num2:
        print(f"{num1} is second largest number")
    else:
        print(f"{num2} is second largest number")





