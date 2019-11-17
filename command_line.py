from sys import argv
print("Python program")
print("Enterd Command Line Argument: ",argv)
print("Length of command line argument:",len(argv))
print("Command line argument one by one:")
for x in argv:
    print(x)
print("Enterd Values :",argv[1:])
print("Addition of Command line argument")
sum=0
args=argv[1:]
for m in args:
    n=int(m)
    sum+=n
print("Addition of Command line argument:",sum)
    
    
    

