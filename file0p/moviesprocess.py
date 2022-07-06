fread=open("movies.txt")
all_movies=[movies.rstrip("\n").split(",") for movies in fread]
print(all_movies)

# number of moviews released in 2022

no_mov_2022= [mov for mov in all_movies if mov[1]=="2022" ]
print(no_mov_2022)
print (len(no_mov_2022))


# number malayalam movies

mala_mov=[mov for mov in all_movies if mov[3]=="malayalam"]
print(mala_mov)

# theater released movies

theyater_mov=[mov for mov in all_movies if mov[-1]=="theater"]
print(theyater_mov)

# list of movies whose rating > 5
rating_five=[mov for mov in all_movies if mov[2]>="5"]
print(rating_five)

# {2022:,4,2021:6,2020:2}

mov_list={}
for mov in all_movies:
    year=mov[1]
    if year in mov_list:
        mov_list[year]+=1
    else:
        mov_list[year]=1
print(mov_list)

# 2021

