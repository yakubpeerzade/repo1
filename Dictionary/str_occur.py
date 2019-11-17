s=input("Enter Dictionary:")
d={}

for x in s:
    d[x]=d.get(x,0)+1

for k,v in d.items():
    print("Word:",k,"Occurence:",v)

