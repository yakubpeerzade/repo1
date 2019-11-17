#Dictionary program

studs={}
n=int(input("Enter number of students:"))
i=0

while i<n:
    name=input("Enter Student Name:")
    marks=input("Enter marks in % :")
    studs[name]=marks
    i=i+1
print("***Student Details***")
for x in studs:
    print("Name:",x,"\t\tMarks:",studs[x])
