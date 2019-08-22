def fib(n):
    p=0
    q=1
    for i in range(n):
        print(p,end=' ')
        r=p+q
        p=q
        q=r
n=int(input("Enter the limit:"))
fib(n)
