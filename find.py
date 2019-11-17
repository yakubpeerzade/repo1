s=input("Enter Main string")
s1=input("Enter string to find")
l=s.find(s1)
if l>=0:
    print("String '{}' found at location={}".format(s1,l))
d=input("Enter Date:")
l=d.split('-')
print(l)

