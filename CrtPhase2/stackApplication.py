stack=[]
s=input("Enter string:")
for i in s:
    if i=='(':
        stack.append(i)
    elif i==')' and len(stack)==0:
        print("Invalid")
        break
    elif i==')' and len(stack)!=0:
        stack.pop()
if len(stack)==0:
    print("Valid")
else:
    print("Invalid")
