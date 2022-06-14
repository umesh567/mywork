students=["ram","ravi","hari","tom","nikil","jain","john"]
passed_students=["ravi","hari","tom"]

#failed students

failed_students=(set(students)).difference(set(passed_students))
print(failed_students)