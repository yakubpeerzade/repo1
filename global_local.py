import random
x="This is global variable"

def Myfunc():
    x="This is local variable"
    print(x)
Myfunc()
print(x)

print("Random Number")
print(random.randrange(1,7))
