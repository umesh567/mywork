lst = [
    [10, 11],
    [13, 45],
    [50, 15],
    [60, 16]
]

#if num>25 num+1 else num -1


flatn_list=[num for sub_list in lst for num in sub_list]
print(flatn_list)

maped_list=[num+1 if num>25 else num-1 for num in flatn_list]
print(maped_list)

even_no=[num for num in flatn_list if num%2==0 ]
print(even_no)
