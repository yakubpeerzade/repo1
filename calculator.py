def add(n1,n2):
    res=n1+n2
    return res
def sub(n1,n2):
    res=n1-n2
    return res
def mul(n1,n2):
    res=n1*n2
    return res
def div(n1,n2):
    if n1==0 or n2==0:
        print("We cannot divide with zero")
        calculator()
    else:
        res=n1/n2
        return res
def calculator():
    num1=int(input("Enter Number One:"))
    num2=int(input("Enter Number Two:"))
    choice=int(input("\n1)Additin\n2)Substraction\n3)Multiplication\n4)Divsion\n5)Exit\n6)clear\nEnter Your choice:"))
    if choice==1:
        print("Addition =",add(num1,num2))
    elif choice==2:
        print("Substraction =",sub(num1,num2))
    elif choice==3:
        print("Multiplication =",mul(num1,num2))
    elif choice==4:
        print("Division=",div(num1,num2))
    elif choice==5:
        exit()
    elif choice==6:
        print("Reset")
        calculator()
    
calculator()        
