students=[]# can store objects
class Student:
    def __init__(self):  #constructor method 
        self.name=None   #with this we create empty constructur 
        self.number=None
        self.age=None
        self.gender=None

    def Add(self,name,number,age,gender):  #with this method we can  add name, number, age, gender in a object  
        self.name=name
        self.number=number
        self.age=age
        self.gender=gender
        sub=[self.name,self.number,self.age,self.gender]  #can store object values 
        students.append(sub) #crete array inside array

    def Display(self):
         print("Students : ",self.name,self.number,self.age,self.gender) #display calling object name ,number , age,gender
 
    
    def Search(self,number): #search metod is looking given student number exist or not 
        self.number=number
        self.student=None
        for nums in students: #looping student array also every nums value equal another array
            if nums[1]==self.number: #nums[1] is students number place in array we are looking given number equala any value 
               self.student=nums  
               #print(nums)

    def Delete(self,number):#delete method remove that value
        self.number=number
        self.Search(number)   #we are calling search method and looking that value is exist or not   
        students.remove(self.student) #if it is exist than remove that student
        print(students)
        

    def  Update(self,number,new_number):  #updateing number value students
          self.number=number #which number we want to change
          self.new_number=new_number #this is the new number
          self.Search(number) #call search method 
          self.student[1]=new_number #replace new number 
          print(self.student)

s1=Student()  #create s1 object
s2=Student()   #create s2 object
s3=Student()   #create s3 object
s1.Add("Alex",3008,20,"Male")  #give value s1 object
s2.Add("Helen",2045,21,"Female")  
s3.Add("Jake",1988,21,"Male")
s1.Display()  
s2.Display()
s3.Display()
s1.Search(s3.number) #s3.number exist or not we searching if exist than print 
s1.Delete(s3.number)  # which student have s3.number value is removing  
s1.Update(s2.number,13)  # which student s2.number value is changeing number value as 13

'''''
output is :
    Students :  Alex 3008 20 Male
    Students :  Helen 2045 21 Female
    Students :  Jake 1988 21 Male
    #['Jake', 1988, 21, 'Male']
    [['Alex', 3008, 20, 'Male'], ['Helen', 2045, 21, 'Female']]
    ['Helen', 13, 21, 'Female']
'''''
