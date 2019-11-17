s=input('Enter String:')
s1=''
s2=''

for x in s:
    if x.isalpha():
        s1=s1+x
    elif x.isdigit():
        s2=s2+x
print(s1+s2)
res=''
for x in sorted(s1):
    res=res+x
for x in sorted(s2):
    res=res+x
print(res)
