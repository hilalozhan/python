class Inflation:
    def __init__(self ,startcoast,endcoast):
        self._startcoast=startcoast
        self._endcoast=endcoast
        self._rate=None

    @property
    def endcoast(self):
         return self._endcoast

    @endcoast.setter
    def endcoast(self,value):
        if value<=0:
           raise ValueError('The age must be positive')
 
      # Cash calculated properties
      # Same value is not calculate again

        if value != self._endcoast:
            self._endcoast=value
            self._rate=None
         

    @property
    def rate(self):
        if self._rate  is None:
            self._rate= ((self._endcoast-self._startcoast)/self._startcoast)*100
       
        return self._rate 

inf=Inflation(102,98)
print(inf.rate)  #output :-3.9215686274509802

inf.endcoast=-20 #output: ValueError: The age must be positive



