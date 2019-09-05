import random
import string
def func1():
    chars=string.ascii_letters+string.digits+'!@#$%^&*'
    size=random.randint(8,12)
    return "".join(random.choice(chars) for i in range(size))
print("1.New password:")
print("2.Exit")
print("Enter your choice:")
ch=int(input())
while(ch==1):
    print("Password:",func1())
    print("Enter your choice:")
    ch=int(input())
    

