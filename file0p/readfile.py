#f=open("abc.txt.")

# for line in f:
#     print(line)


#writing

f=open("abc.txt","w")

lst=["python","javascripct","c#","umesh"]
company_name="luminar"

for line in lst:
    line+="\n"
    f.write(line)
