#concatinating two string
s1=input('Enter String 1:')
s2=input('Enter String 2:')
print('Conactinating two string using + operator')
s3=s1+' '+s2
print('Concatinated String:',s3)
i,j=0,0
s4=''
while i<len(s1):
    s4=s4+s1[i]
    i=i+1
s4=s4+' '
while j<len(s2):
    s4=s4+s2[j]
    j=j+1
print('Concatinated String:',s4)
