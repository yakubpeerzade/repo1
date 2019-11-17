'''def calc(a,b,c):
    if c==1:
        print("Addition Of Number:",a+b)
    elif c==2:
        print("Substrction of Number:",a-b)
    elif c==3:
        print("Multipliacation of Number:",a*b)
    elif c==4:
        print("Divsion of number:",a/b)
    else:
        print("Invalid Choice")
        exit()
a=int(input("Enter Number1:"))
b=int(input("Enter Number2:"))
c=int(input("Enter Your choice: \n1)Addition \n2)Substraction\n3)Multiplication\n4)Divsion\n"))
calc(a,b,c)'''

def cal(a,b,c):
    if c==1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    elif c==4:
        return a/b
    else:
        print("invalid choice")
n1=int(input("Enter Number 1:"))
n2=int(input("Enter Number 2:"))
n3=int(input("1)Addition\n2)Substraction\n3)Multiplication\n4)Division\n5)Result of all operation\nEnter Your choice:"))

if n3==5:
    for x in range(1,5):
        j=cal(n1,n2,x)
        print(j)
else:
   j=cal(n1,n2,n3)
   print(j)
    


