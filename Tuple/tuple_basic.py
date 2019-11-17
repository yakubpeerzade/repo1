t=tuple()
print("Empty Tuple:",t)
s=input("Enter Element in tuple:")
s=s.split(' ')
t1=[]
type(t1)
for x in s:
   t1.append(int(x))  
print(t1)
print(type(t1))
print("ELements in Tuple:")
for x in t1:
    print(x)
print("Slice operator:")
print(t1[0:6])
t2=(20,30,50,90,1000)



