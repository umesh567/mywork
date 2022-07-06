#sorting dict based on values

word_count={"a":2,"b":5,"c":2,"d":4,"e":2}

Wc_lst=word_count.items()    #word_count dict ne oru list of tuple akki convert chythu

print(sorted(Wc_lst,key=lambda item:item[1],reverse=True))


#find maximum value  #max()

print(max(Wc_lst,key=lambda l:l[1]))

print(min(Wc_lst,key=lambda l:[1]))
