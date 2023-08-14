text="hello my name is hilal"
letters=list(text)
count={}
for letter in  letters:
    if letter in count:
        count[letter]+=1
    else :
        count[letter]=1

for letter ,n in count.items():
    print(letter," tekrar sayısı : ",n)

