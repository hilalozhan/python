class Counter:

    counter =0

    def increse(self):
        self.counter += 1
    
    def value(self):
        return self.counter
   
    def reset(self):
       self.counter=0

count=Counter()
count.increse()
print(count.value()) # output is: 1
count.reset()

i = 0
while i<5:
     count.increse()
     i+=1

print(count.value()) #output is : 5    
        
