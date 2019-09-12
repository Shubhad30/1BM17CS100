class student:
    def __init__(self):
        self.__sid=None
        self.__sage=None
        self.__smarks=None
    def validate_smarks(self):
        if(self.__smarks>=0 and self.__smarks<=100):
            return True
        else:
            return False
    def validate_sage(self):
        if(self.__sage>=20):
            return True
        else:
            return False
    def check_qualification(self):
        op1=self.validate_smarks()
        op2=self.validate_sage()
        if(op1==True and op2==True):
            if(self.__smarks>=65):
                return True
            else:
                return False
        else:
            return False
    def setter(self,i):
        print("\nEnter Details for student",(i+1),":")
        self.__sid=int(input("Enter the student id:"))
        self.__smarks=int(input("Enter the student's marks :"))
        self.__sage=int(input("Enter the student age:"))
    def getter(self,i):
        print("\nSTUDENT",(i+1),":")
        print("Student id:",self.__sid)
        print("Student marks:",self.__smarks)
        print("Student age:",self.__sage)
        str="U are Qualified...." if(self.check_qualification()) else "Sorry!! Not Qualified..\nInvalid age or invalid marks.."
        print(str)
n=int(input("Enter no of students:"))
s=[student() for i in range(n)]
for i in range(n):
    s[i].setter(i)
for i in range(n):
    s[i].getter(i)

        
    
