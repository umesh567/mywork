class employee():
    eid=int
    ename=str
    role=str

    def __init__(self,**kwargs):
        self.eid=kwargs.get("eid")
        self.ename=kwargs.get("ename")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.ename


class Batch():
    def __init__(self,**kwargs):
        self.bid=kwargs.get("bid")
        self.bname=kwargs.get("bname")
        self.user=kwargs.get("user")

    def __str__(self):
        return self.bname

employee=employee(eid="1001",ename="vishnu",role="NA")
Batch=Batch(bname="dyjango",role="NA")
print(employee)
print(Batch)