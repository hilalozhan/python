students=[]           
class Student:
    
     def __init__(self,name,number,age,gender):
         self.name=name
         self.number=number
         self.age=age
         self.gender=gender 

     def Add(self):
         self.name=input("Please enter name:  ")
         self.number=int(input("Please enter number: "))
         self.age=int(input("Please enter age: "))
         self.gender=input("Please enter gender: ")
         sub=[self.name,self.number,self.age,self.gender]
         students.append(sub)
      
     def Display(self):
         print("Students : ",self.name,self.number,self.age,self.gender)
 

s1=Student("Adrean",1102,20,"Male")
s2=Student("Helga",1006,21,"Female")
students=[[s1.name,s1.number,s1.age,s1.gender],[s2.name,s2.number,s2.age,s2.gender]]


def Search():
     num=int(input("Please enter number for search :"))
     for nums in students:
          if nums[1]==num:
              print(nums)
    
def Delete():
      num=int(input("Please enter number for delete :"))
      for nums in students:
          if nums[1]==num:
              students.remove(nums)
              print(students)

def Update():
      num=int(input("Please enter number for update :"))
      for nums in students:
          if nums[1]==num:
              new_num=int(input("Please enter new number: "))
              nums[1]=new_num
              print(students)


s3=Student("",0,0,"")
s3.Add()
s3.Display()
s1.Display()
s2.Display()
Search()
Delete()
Update()

'''''
output is :
    Please enter name:  Ashley
    Please enter number: 1890
    Please enter age: 23
    Please enter gender: Female
    Students :  Ashley 1890 23 Female
    Students :  Adrean 1102 20 Male
    Students :  Helga 1006 21 Female
    Please enter number for search :1102
    ['Adrean', 1102, 20, 'Male']
    Please enter number for delete :1102
    [['Helga', 1006, 21, 'Female'], ['Ashley', 1890, 23, 'Female']]
    Please enter number for update :1006
    Please enter new number: 2009
 [['Helga', 2009, 21, 'Female'], ['Ashley', 1890, 23, 'Female']]
