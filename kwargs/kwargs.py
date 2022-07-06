def add(*args):
    return sum(args)

def max_fun(*args):
    return max(args)

def min_fun(*ar):
    return min(ar)




def add_nums(**kwargs):
    print(sum([v for v in kwargs.values()]))

add_nums(n1=10,n2=20,n3=40)



def sort_num(**kwargs):
    print(sorted([v for v in kwargs.values()]))

sort_num(n1=40,n2=89,n3=50)







#dict.ites()