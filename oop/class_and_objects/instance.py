
class Class:
    # This is a method because it is have access in an object 'self'
    def __init__(self,name,num,sum_notes):
        self.name=name
        self.num=num
        self.sum_notes=sum_notes

    def note_average(self):
        print(self.sum_notes/self.num)

    # This is a function 
    def intro():
        print("This class average is : ")


classs=Class("10-B",20,180)
Class.intro()
Class.note_average(classs)
#output : " This clas average is :  9.0 "



        

