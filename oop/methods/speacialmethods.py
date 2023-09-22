class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age

 # __str__ operater is  human readeble  
 #__repr__ operater is machine readeble

    def __repr__(self):   
        return f'Person("{self.name}","{self.surname}","{self.age}")'

    def __str__(self):
        return f'({self.name},{self.surname},{self.age})'

    def func(self):
       return f'Person({self.name},{self.surname},{self.age})'

# compare two objects by their values  

    def __eq__(self,other):
        return self.age==other.age

    def __hash__(self):
        return hash(self.age)

    def __bool__(self):
         if self.age < 18 or self.age > 65:
             return False 
         return True
    
    def __del__(self):
        print('del was called')

person=Person("John","MC",54)
print(Person.func(person)) #output: Person(John,MC,54)
print(person) #output :  (John,MC,54)
print(repr(person)) #output: Person("John","MC","54") 


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)

print(john is jane)  # False
print(john == jane) # True

print(hash(person)) #output: 54 

print(bool(person)) #False

del person #person object deleted

