car={"name":"swift","color":"red","make":"2014","brand":"maruthi","fuel":"petrol","price":"10lak","wheels":"3"}

print(car["name"])

print(car["brand"])

print(car["price"])

print(car["make"])

#cheking a type in car class
print("transmission_type" in car)

#adding new type

car["transmission_type"]="manuel"
print(car)


print("break_type" in car)


car["break_type"]="abs"
print(car)


#updation

print(car["wheels"])

car["wheels"]="4"
print(car)