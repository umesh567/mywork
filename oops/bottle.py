class bottle:
    material: str
    capasity: int
    price: int
    color: str

    def __init__(self, **kwargs):
        self.material = kwargs.get("material")
        self.capasity = kwargs.get("capasity")
        self.price = kwargs.get("price")
        self.color = kwargs.get("color")

    def print_bottle(self):
        print(self.material, self.capasity, self.color, self.price)


b = bottle(material="plastic", capasity="500", color="red")
b.print_bottle()

# class bottle:
#     def __init__(self,**kwargs):
#         self.material=kwargs.get("material")
#         self.price=kwargs.get("price")
#
#     def print_bottle(self):
#         print(self.material,self.price)
#
# b=bottle(material="plastic",price=500)
# b.print_bottle()
