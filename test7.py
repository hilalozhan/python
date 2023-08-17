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
        for nums in students:
                if nums[1]==self.number:
                    print(nums)

    def Delete(self,number):
        self.number=number
        for nums in students:
                if nums[1]==self.number:
                    students.remove(nums)
                    print(students)

    def  Update(self,number,new_number):
          self.number=number
          self.new_number=new_number
          for nums in students:
                if nums[1]==self.number:
                    nums[1]=new_number
                    print(nums)

s1=Student()
s2=Student()
s3=Student()
s1.Add("Alex",3008,20,"Male")
s2.Add("Helen",2045,21,"Female")
s3.Add("Jake",1988,21,"Male")
print(students)
s1.Search(s3.number)
s1.Delete(s2.number)
s1.Update(s2.number,13)

'''''
output is :
    [['Alex', 3008, 20, 'Male'], ['Helen', 2045, 21, 'Female'], ['Jake', 1988, 21, 'Male']]
    ['Jake', 1988, 21, 'Male']
    [['Alex', 3008, 20, 'Male'], ['Jake', 1988, 21, 'Male']]

