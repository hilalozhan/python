students=[]
class Student:
    def __init__(self):
        self.name=None
        self.number=None
        self.age=None
        self.gender=None

    def Add(self,name,number,age,gender):
        sub=[self.name,self.number,self.age,self.gender]
        students.append(sub)

s1=Student()
s1.Add("Alex",3008,20,"Male")
print(students)

