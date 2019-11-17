s=input("Enter String:\n")
l=s.split()
l1=[]
i=len(l)-1

while i>=0:
    l1.append(l[i])
    i=i-1
res=' '.join(l1)
print(res)
        
print("Making Original string")

res2=' '.join(reversed(res.split()))
print(res2)
