#lst=[10,10,10,4,5,6,6,9,8,8,7,2,2]
#duplicates want to remove so list is changed to set

#st=set(lst)
#print(st)

#print(dir(set))
########################################################################################


set1={1,2,3,4,5,}
set2={10,11,12,2,3}
#set1.add(10)           for adding value in set
print(set1)

#union

union_set=set1.union(set2)
print(union_set)

#intersection

intersection_set=set1.intersection(set2)
print(intersection_set)


diff_set=set1.difference(set2)
print(diff_set)

#difference of set set 2 ile ulla set1 same elements remoove ayii bakkiyulla values display cheyyum



#updation

set3={300,400,500}
set1.update(set3)
print (set1)
