def func1(l1,key1):
    if key1 in l1:
        return "True"
    return "False"
n=int(input("Enter the limit:"))
l=[]
for i in range(n):
    n1=int(input())
    l.append(n1)
key=int(input("Enter the key element :"))
ans=func1(l,key)
print(ans)
