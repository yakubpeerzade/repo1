#program to count lenght of string

s=input("Enter String")
l=len(s)
print("Length of String={} length={}".format(s,l))
print("Printing string in reverse order:")
i=-1
while i>=-l:
    print(s[i],end='')
    i=i-1
if 'y' in s:
    print("\nThe word contains y")
if 'yakub' in s:
    print("it's {}".format(s))
if 'peerzade' in s:
    print("My surname is there")
s1=input("Enter String 2:")

if s>s1:
    print("String 1 is bigger than string 2")
elif s1>s:
    print("String 2 is bigger than string 1")
else:
    print("Both string are equal...")
print("Strip program(removing space)")
n=input("Enter String")
print("Right Strip")
c1=n.rstrip(n)
print(c1)
print("Left Strip:",n.lstrip(n))
print("Strip:",n.strip(n))




    

