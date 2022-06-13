mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]

# q1 total number of out_of_stock mobiles

#out_stock_product=[mob for mob in mobiles if mob[-1]==0]
#print(len(out_stock_product))

# q2 total stock

#avl_stock=[mob[-1]]for mob in mobiles:
 #   print

# q3 pritn mobiles available in range 20k to 30k

#range_stock=[mob for mob in mobiles if mob[4] in range (20000,30000)]
#print(range_stock)

# q4 print all 5g phone

#five_g=[mob for mob in mobiles if mob[2]=="5g"]
#print(five_g)

# q5 print samsung mobiles
samsung_mob=[mob for mob in mobiles if mob[-2]=="samsung"]
print(samsung_mob)



# q6 print costly mobile

max_prices=max([mob[4] for mob in mobiles])
costly_pro=[mob for mob in mobiles if mob[4]==max_prices]
print(costly_pro)

# q7 prin low cost mobiles

mobiles.sort(reverse=True,key=lambda mob:mob[4])
print(mobiles)


# q8 print all mobiles having stock >10

stock_gt=[mob for mob in mobiles if mob[-1]>10]
print(stock_gt)

# q9 count of mobiles having dispaly amoled
count_amo=[mob for mob in mobiles if mob[3]=="AMOLED"]
print(count_amo)
print(len(count_amo))

# q10 sort mobiles based on price oredr by desc

# q11 sort mobiles based on avl stock oredr by desc

# q12 is there any mobile available at rs 10000 ?

mob_ten=[mob[4]==10000 for  mob in mobiles ]
print("available"if True in mob_ten else "no")

# q12 list all mobiles having same price



#flattern_list=[num for sub_list in mobiles for num in sub_list]
#print(flattern_list)