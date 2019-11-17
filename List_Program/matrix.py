print("This is matrix program")

m=[[10,20,30],[40,50,60],[70,80,90]]
print(m)

for x in m:
    print(x)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j],end=' ')
    print()
    


