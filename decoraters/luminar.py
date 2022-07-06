#moone class create cheyyunnu staff course batch


class staff():
    id:int
    name:str
    role:str


    def __init__(self,**kwargs):
        self.id=kwargs.get("id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
       return self.name


staff=staff(id=100,name="rahul",role="admin")
print(staff)