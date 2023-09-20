class Person :  # Create a class
      pass

p1=Person() # To create an instance of a class

print(p1) # output: <__main__.Person object at 0x00000273B3C6EBD0>  , Name and memory adress
print (id(p1))  #output : 2359891520336  , To get an identity of an object

print (isinstance(p1,Person))  #output: True ,  The p1 object is an instance of the Person class


class Document:
    extension= 'html'
    version='5'

# Get the values of class variables
print(Document.extension) # html
print(Document.version) # 5

#Another way to get the value of a class variable is to use the getattr() function

extension = getattr(Document, 'extension')
version = getattr(Document, 'version')

print(extension)  # html
print(version)  # 5


#Set values for class variables

Document.version= 10
setattr(Document,'version',10)

#Delete class variables
delattr(Document,'version')
#del Document.version



# Class variables storege
from pprint import pprint

class Employee:
    name='john'
    age='30'

pprint(Employee.__dict__)
#output is:
# mappingproxy({'__dict__': <attribute '__dict__' of 'Employee' objects>,
                           # '__doc__': None,
                           # '__module__': '__main__',
                           # '__weakref__': <attribute '__weakref__' of 'Employee' objects>,
                           # 'age': '30',
                           # 'name': 'john'})


