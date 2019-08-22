n=int(input("Enter the limit:"))
print("Enter the elments:")
l1=list([])
for i in range(n):
    n1=int(input())
    l1.append(n1)
l2=[ele for ele in l1 if(ele%2==0)]
print("Even list:",l2)
