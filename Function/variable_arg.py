def mul(*n):
    total=1
    for n1 in n:
        total=total*n1
    print("Multiplicatin of number:",total)
def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("Sum of number:",total)
def prin(*a,k):
    print("Variabe length argument:")
    for x in a:
        print(x)
    print("Formal argument:")
    print(k)

sum(10,20)
sum(10,20,230,40,679,78)
#Mutiplication of number
mul(10,20)
mul(10,20,30,40)
prin("A","B","C","D",k=20)
prin('x','y','z',k=10)
