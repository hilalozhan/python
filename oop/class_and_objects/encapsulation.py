class Person :
    def __init__(self,name,surname,age,id_num):
        self._name=name  # Name is private
        self.surname=surname
        self.age=age
        self._id_num=id_num  # Id number is  private 

    def _add(self,country):  #Private method
        self.country=country 
     
    def getName(self):
        print (self._name ,self.surname)

    def setName(self,new_name):
        self._name= new_name
     
person=Person("Jane","Austen",21,110090)
person.getName()  # output :  Jane Austen
person.setName("Camilla")
person.getName()   # output: Camilla Austen



