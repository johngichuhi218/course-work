class Zetech:
    def students(self):
        print("I am a student at zetech university.")
        
    def course(self):
        print("My course is BSCIT.")
        
class Unit(Zetech):
    def home(self):
        print("The unit is called python programming.")
        
        
class Account(Unit, Zetech):
    def fees(self):
        print("I have already paid the fees.")
    
        

d = Account()
d.fees()
d.home()
d.students()
d.course()