s=input("Enter String:")
print(len(s))
i=len(s)-1
target=''

while i>=0:
    target=target+s[i]
    print(target)
    i=i-1
print(target)
