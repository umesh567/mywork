#class:   blueprint,plan ,dp

#object realworld entity

#class creation

# class person:
#     name:str
#     age:int
#     gender:str
#     def set_person(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def print_person(self):
#         print(self.name,self.age,self.gender)
#
# p=person()
# p.set_person("ram","34","m")
# p.print_person()


class person:
    name:str
    age:int
    gender:str
    def set_person(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print_person(self):
        print(self.name,self.age,self.gender)

p=person()
p.set_person("ram","34","m")
p.print_person()