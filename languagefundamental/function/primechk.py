
def is_prime(num):
    flag=0
    for i in range (2,num):
        if(num%i==0):
            flag=1
            break
    return flag==0
print(is_prime(5))


def prime_range(low,upp):
    for num in range(low,(upp+1)):
        if is_prime(num):
            print(num)
print (prime_range(10,55))


