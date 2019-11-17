l=[x*x for x in range (1,11)]
print(l)

print("Squares till 20,Eve numbers only")
l2=[x**2 for x in range(1,21) if x%2==0]
print(l2)

s=input("Enter some strings")
s=s.split()
print(s)

l1=[w[0] for w in s]
print(l1)

l3=[w for w in s if len(w)>=5]
print(l3)



