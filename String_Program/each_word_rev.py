s=input("Enter String:")
l=s.split()
l1=[]
i=0

while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
    print(i)
    
res=' '.join(l1)
print(l1)
print(res)
