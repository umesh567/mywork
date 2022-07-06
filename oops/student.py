class student:
    roll_no:int
    name:str
    gender:str
    std:int
    def set_student(self,roll_no,name,gender,std):
        self.roll_no=roll_no
        self.name=name
        self.gender=gender
        self.std=std
    def print_student(self):
        print(self.roll_no,self.name,self.gender,self.std)

s1=student()
s2=student()
s1.set_student(1001,"manu","M",8)
s1.print_student()
s2.set_student(2001,"vbd","f","4")
s2.print_student()
