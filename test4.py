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

'''
output is :
    h  tekrar sayısı :  2
    e  tekrar sayısı :  2
    l  tekrar sayısı :  4
    o  tekrar sayısı :  1
       tekrar sayısı :  4
    m  tekrar sayısı :  2
    y  tekrar sayısı :  1
    n  tekrar sayısı :  1
    a  tekrar sayısı :  2
    i  tekrar sayısı :  2
    s  tekrar sayısı :  1

 '''  
