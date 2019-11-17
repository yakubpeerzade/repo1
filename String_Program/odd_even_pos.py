#program for odd even position of string

s=input("Enter String:")
print(s[::2])
print(s[1::2])

#Method 2 for priting odd even postion of string

i=0
while i<len(s):
    if i%2==0:
        print("Even Position:",i,":",s[i].format(i))
        i=i+1
    else:
        print("Odd Position:",i,":",s[i].format(i))
        i=i+1

