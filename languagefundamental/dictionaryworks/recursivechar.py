pattern="ABACBCD"

#PRINT FIRST RECURSIVE NO::::::::::::::

#char_count={}

#for char in pattern:
 #   if char in char_count:
  #      print("first recursive",char)
   #     break
   # else:
    #    char_count[char]=1


#second recursive no:::::::
char_count={}   #character count

#forming a list
rec_char=[]            #recursive character ine vendi ulla list
for char in pattern:
    if char in char_count:
        rec_char.append(char)
    else:
        char_count[char]=1
print(rec_char[1],"sec rec char")