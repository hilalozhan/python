class Object:
    
    @staticmethod
    def area(r,pi):
        return   pi * pow(r,2)

    @staticmethod
    def volume(r,pi):
        return  4/3* pi * pow(r,3)

print(Object.area(3.22,3.14) )  # output is : 32.556776000000006
print(Object.volume(5,3.14)  )  # output is : 523.3333333333334 
