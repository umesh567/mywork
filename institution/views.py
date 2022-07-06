class course:
    course_name: str
    active_status: bool


    def add_course(self, **kwargs):
        self.course_nmae = kwargs.get("course_name")
        self.active_status = kwargs.get("active_status")


    def __str__(self):
        return self.course_nmae



class batch:
    course:course
    batch_code:str
    start_date:str

    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code

class student:
    student_name:str
    gender:str
    rol:str
    batch:batch

    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.rol=kwargs.get("rol")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.student_name




django=course()
django.add_course(course_name="django",active_status=True)

bigdata=course()
bigdata.add_course(course_name="bigdata",active_status=True)

print(django)
print(bigdata)

db1=batch()
db1.add_batch(course=django,batch_code="djmay2k22",start_date="5-6-2022")

db2=batch()
db2.add_batch(course=bigdata,batch_code="djmay2k22",start_date="5-6-2022")

print(db1)
print(db2)

rahul=student()
rahul.add_student(student_name="rahul",gender="male",rol="2345",batch=db1)

akshai=student()
akshai.add_student(student_name="akshai",gender="male",rol="2346",batch=db1)

nikhil=student()
nikhil.add_student(student_name="nikhil",gender="male",rol="2347",batch=db2)

print(rahul)
print(akshai)
print(nikhil)

print(rahul.batch.course.course_nmae)