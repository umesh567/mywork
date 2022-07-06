#map
#filter
#reduce


lst=[1,2,3,4]

#list compreshionmethod

# squarrs=[no**2  for no in lst ]   #map
# print(squarrs)

#ithe thanne map function use cheyyumbol

squares=list(map(lambda  n:n**2,lst))
print(squares)

#less<no-1 >5 no+1

# num_out=[num-1 if num<5 else num+1 for num in lst]
# print(num_out)


#map

num_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(num_out)

