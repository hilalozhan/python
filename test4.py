text="hello my name is hilal"
letters=list(text)
count={}  # this is an empty array for letters repeat time 
for letter in  letters:
    if letter in count: #it is looks inside count array and if there have any key then it is added value one more
        count[letter]+=1
    else : # if array dont have kind a key than it is give a value for that key 
        count[letter]=1

for letter ,n in count.items():   #count.item is search key-value pair and take the value and repet time  
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
