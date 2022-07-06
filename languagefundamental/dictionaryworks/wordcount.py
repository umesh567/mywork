text="hai hello hai hello"

#split method

words=text.split(" ")     #space veche text ine split chythe words il store cheyyunnu
word_count={}
for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)

