def countparenthesis(str1):
    stack=[]
    dict1={"(":")","{":"}","[":"]"}
    for i in str1:
        if i in dict1:
            stack.append(i)
        elif len(stack)==0 or dict1[stack.pop()]!=i:
            return False
    return len(stack)==0
str=input("Enter the expression:")
ans=countparenthesis(str)
if ans:
    print("Valid Expression..")
else:
    print("Invalid Expression..")
