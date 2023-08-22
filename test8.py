'''''
Recursive : Function calls itself
Stack: Last in first out
'''''

stack=[3,4,6,7,5]

def add(s,num):
    #base case stack is empty or not
      if len(s) == 0:
        s.append(num)

      else:
        x = s.pop() 
        add(s, num)
      #put back removed item
        s.append(x)
 

    
def sort(s):
    if len(s) !=0:
        x=s.pop()
        sort(s)
        add(s,x) 
sort(stack)
print(stack)

'''''
output is :
    [5, 7, 6, 4, 3] 
'''''
   
