'''''
Recursion: function calls itself
Stack : last in first out
'''''

stack=[3, 4, 6, 7, 5]

def sort(s):
    temp=[]
    if len(s)!=0:
     x=s.pop()
     temp.append(x)
     print(temp)
     sort(s)
     
         

sort(stack)

'''''
output is : 
    [5]
    [7]
    [6]
    [4]
    [3]
'''''

