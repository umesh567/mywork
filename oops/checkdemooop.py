# class umesh:
#   age:int
#  gender:str
# fam:str
# def set_umesh(self,age,gender,fam):
#   self.age=age
#  self.gender=gender
# self.fam=fam
# def print_umesh(self):
#    print(self.age,self.gender,self.fam)

# p1=umesh()
# p2=umesh()
# p1.set_umesh("56","male","kochu")
# p2.set_umesh("45","f","kachu")
# p1.print_umesh()
# p2.print_umesh()


class umesh:
    age: int
    gender: str
    fam: str

    def __init__(self,**kwargs):  #set method ine pakaram __init__ use cheyyunnu
        self.age = kwargs.get("age")
        self.gender =kwargs.get("gender")
        self.fam = kwargs.get("fam")

    def print_umesh(self):
        print(self.age, self.gender, self.fam)


p1 = umesh(age="56",gender= "male",fam= "kochu")
p1.print_umesh()
