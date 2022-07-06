# students=open("students.txt")
# all_students=[stud.rstrip("\n") for stud in students]
# f_student=open("failed.txt")
# failed_student=[stud.rstrip("\n") for stud in f_student]
# passed=open("passed.txt","w")
#
# passed_students=set(all_students)-set(failed_student)
# print(passed_students)
# for st in passed_students:
#     passed.write(st)

students=open("students.txt")
all_students=[stud.rstrip("\n") for stud in students]  #file open akki ennitte athine list akki
f_student=open("failed.txt")
failed_students=[stud.rstrip("\n") for stud in f_student]
passed=open("passed.txt","w")

passed_students=set(all_students)-set(failed_students)
print(passed_students)

for st in passed_students:
    st+="\n"   #same line il varathy irikkan ane iggane chythekkunnathe.
    passed.write(st)