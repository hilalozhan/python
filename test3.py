my_list=[1,2]

my_list.append (5)
my_list.append(8)
#.append is adding value in list in order

#print(my_list[0]+my_list[3])
 # output is "9"

name="Luna"

#print("hello my name is %s"%name)
 #output is "hello my name is Luna"

lotsofhellos = "hello" * 10
#print(lotsofhellos)

#output is "hellohellohellohellohellohellohellohellohellohello"

text="hello my name is luna"
harfler = list(text)
#print(harfler)
count=0

for x in harfler:
    if x=='a':
        count+=1

#print("a harfinden",count,"adet var")

#output is "a harfinden 2 adet var"



new_text="hilal"
letters=list(new_text)

for a in letters:
   counter=0
   for b in letters:
      if a==b:
        counter+=1
   print (a,counter)  

'''
output is =
h 1
e 1
l 2
l 2
o 1
'''


