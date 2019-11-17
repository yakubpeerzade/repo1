print("We figure out list==Array")
a=[]
n=int(input("Enter Number of element you want to add in array:"))
for i in range(n):
    e=int(input("Enter number "))
    a.append(e)
print(a)
print("Additon of list")
sum=0
for x in a:
    sum+=x
print("Sum of list:",sum)    
