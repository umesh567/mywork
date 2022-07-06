class p1:
    def m1(self):
        print("inside m1")


class p2(p1):
    def m2(self):
        print("inside m2")



class p3(p2):                 #class p3(p2,p1) is called muliple inheritance
    def m3(self):
        print("inside m3")

p3=p3()
p3.m3()
p3.m2()
p3.m1()