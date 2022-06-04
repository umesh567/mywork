def add_numbers(n1,n2):
    return(n1+n2)
print(add_numbers(10,20))



def sub_numbers(n1,n2):
    return n1-n2
print(sub_numbers(5,10))


def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
print(smart_sub(10,5))

def num_chk(num):
    return "even" if num%2==0 else "odd"
print(num_chk(5))





def is_starts_witha(name):
    return name.startswith("a")
name="technolab"
print(name.endswith("lab)"))



def validate_gmail(email):
    return email.endswith("@gmail.com")
print(validate_gmail("abc@gmail.com"))


def factorial(num):
    fact=1
    for i in range (1,(num+1)):
        fact=fact*i
        return fact
print(factorial(6))


    #lambda function
sub=lambda n1,n2:n1-n2
print(sub(100,50))

#cube

cube=lambda n:n**3
print(cube(6))

add=lambda n1,n2:n1+n2
print(add(50,20))


#prime number using function

def prime_chk(num):
    if(num==1):
        return False
    elif(num==2):
        return True
    else:
        for i in range(2,num):
            if(num%i==0):
                return False
            return True
print(prime_chk(13))
