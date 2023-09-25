import re  
'''''
Regex, which is the abbreviation of the word Regular Expressions, is a syntax of its own that enables 
the control of inputs entered by the user in a certain order, such as e-mail address, date, phone number, and the search, finding and management of the desired text or code fragment in any code, text.

'''''

class Parser:
    def __init__(self,text):
        self.text=text
     
    def email(self):
        match=re.search(r'[a-z0-9\.\]+@+[a-z0-9\.\-+_]+\.[a-z]+',self.text)
        if match:
              return match.group(0) # Returns all values that match the given condition
         
         
        return None

     def phone(self):
         match= re.search(r'\d{3}-\d{3}-\d{4}', self.text)
         
         if match:
             return match.group(0)

         return None

     def parse(self):
             return {
                'email': self.email(),
                'phone': self.phone()
                         
                 }

s = 'Contact us via 408-205-5663 or email@test.com'
parser = Parser(s)
print(parser.parse())
