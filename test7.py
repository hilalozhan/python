students=[]
class Student:
    def __init__(self):
        self.name=None
        self.number=None
        self.age=None
        self.gender=None

    def Add(self,name,number,age,gender):
        self.name=name
        self.number=number
        self.age=age
        self.gender=gender
        sub=[self.name,self.number,self.age,self.gender]
        students.append(sub)

    def Display(self):
         print("Students : ",self.name,self.number,self.age,self.gender)
 
    
    def Search(self,number):
        self.number=number
        self.student=None
        for nums in students:
            if nums[1]==self.number:
               self.student=nums
               #print(nums)

    def Delete(self,number):
        self.number=number
        self.Search(number)      
        students.remove(self.student)
        print(students)
        

    def  Update(self,number,new_number):
          self.number=number
          self.new_number=new_number
          self.Search(number)
          self.student[1]=new_number
          print(self.student)

s1=Student()
s2=Student()
s3=Student()
s1.Add("Alex",3008,20,"Male")
s2.Add("Helen",2045,21,"Female")
s3.Add("Jake",1988,21,"Male")
s1.Display()
s2.Display()
s3.Display()
s1.Search(s3.number)
s1.Delete(s3.number)
s1.Update(s2.number,13)

'''''
output is :
    Students :  Alex 3008 20 Male
    Students :  Helen 2045 21 Female
    Students :  Jake 1988 21 Male
    #['Jake', 1988, 21, 'Male']
    [['Alex', 3008, 20, 'Male'], ['Helen', 2045, 21, 'Female']]
    ['Helen', 13, 21, 'Female']
'''''
