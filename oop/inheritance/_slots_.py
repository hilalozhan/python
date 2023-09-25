'''''
Usage slots: 
    * Slots use less memory becuse use tuple instead of dict ,
    also this way elements is limited and we can't expend it as we wish . 

    * Don’t specify the attributes that are already specified in the __slots__ of the base class.
     

'''''

class Person:
    _slots_=('name','surname')

    def __init__(self,name,surname):
        self.name=name
        self.surname=surname


    def __repr__(self):
        return f'Point2D({self.x},{self.y})'


person=Person('John','Wick')
print(point.__dict__)
#AttributeError: 'Person' object has no attribute __dict__

print(point.__slots__)
#('John','Wick')







