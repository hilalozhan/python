file=open("helloworld.txt","r")  #with open function file is opening and with "r" we can only read file

for line in file:  # we take every line in file 
    words=line.split()  #we separate lines at each space
        for word in words :  # we print every word in line 
                     print (word)

'''''
output is :
    hello
    world
 
''''' 
