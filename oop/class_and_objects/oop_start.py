class Person:   #We careate a class
  
     counter=0

     def __init__(self,name,age):
         self.name=name
         self.age=age
         Person.counter +=1

     def greet(self):
         return f"Hello ,it's {self.name}"

###Class Methods 

     @classmethod

     def create_anonymous(cls):
         return Person('Anonymous',30)



p1=Person("John",25) #create an object
p2=Person("Helen",22) 
print(p1.greet())  #output: "Hello it's John"
print(Person.counter) #output : 2

anonymous=Person.create_anonymous()  #Call classmethod
print(anonymous.name) # output is : "Anonymous"


###Static Methods 

class Temprature:
    @staticmethod 
    def celcius_to_fahrenheit(c):
        return 9 * c / 5 + 32

celcius=Temprature.celcius_to_fahrenheit(30)
print(celcius) #output is: 86

###Single İnheritance 

class Employee(Person):
    def __init__(self,name,age,job_title):
        super().__init__(name,age)
        self.job_title=job_title

    def greet(self):
        return super().greet() + f"I am a {self.job_title}"


employee= Employee('John',35,'Developer')
print(employee.greet())  #output : Hello ,it's JohnI am a Developer 

