s=input("Enter String:")
pre=''
res=''
i=0
while i<len(s):
    if s[i].isalpha():
        pre=s[i]
        i=i+1
    elif s[i].isdigit():
        res=res+pre*(int(s[i]))
        i=i+1
print(res)
