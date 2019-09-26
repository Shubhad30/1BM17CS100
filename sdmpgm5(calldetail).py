class calldetails:
    def __init__(self,sno,rno,d,t):
        self.sendno=sno
        self.recvno=rno
        self.duration=d
        self.type=t
    def __str__(self):
        return f"\nCalling no:{self.sendno}\nDialled no:{self.recvno}\nDuration:{self.duration}\nType:{self.type}"
class util:
    typecount={"STD":0,"ISD":0,"LOCAL":0}
    def __init__(self):
        self.lofcallob=[]
    def parse_customer(self,lofcallst):
        for i in lofcallst:
            a,b,c,d=i.split(",")
            util.typecount[d]+=1
            self.lofcallob.append(calldetails(a,b,c,d))
    def printdetails(self):
        for i in self.lofcallob:
            print(i)
    def callcount(self):
        for i in util.typecount:
            print("No of",i,"calls:",util.typecount[i])
        

n=int(input("Enter the no of calls:"))
l=[]
for i in range(n):
    print("Enter the details of call:",(i+1))
    sn=input("Enter the calling no:")
    rn=input("Enter the called no:")
    d=input("Enter the duration:")
    t=input("Enter the type:")
    c=sn+","+rn+","+d+","+t
    l.append(c)
u=util()
u.parse_customer(l)
u.printdetails()
print()
u.callcount()



        
