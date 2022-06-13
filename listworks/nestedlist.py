lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]

#print no >16

for sub_lst in lst:
    for num in sub_lst:
        if num>16:
          print(num)

  #flattern list  #arrange nested list in same line

flatten_list=[]
for sub_lst in lst:
    for num in sub_lst:
        flatten_list.append(num)
print (flatten_list)


#one line flatternlist

flatn_list=[num for sub_lst in lst for num in sub_lst]
print(flatn_list)

num_gt_num=[num for num in flatn_list if num>16]
print(num_gt_num)

odd_no=[num for num in flatn_list if num%2!=0 ]
print(odd_no)

even_no=[num for num in flatn_list if num%2==0]
print(even_no)



