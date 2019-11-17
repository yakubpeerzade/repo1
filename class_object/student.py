class student:
    def __init__(self,name,age,rollno,std):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.std=std
    
s1=student('yaqoob',16,157,10)
'''print("name=",s1.name)
print("Age=",s1.age)
print("rollno=",s1.rollno)
print("Standard=",s1.std)'''
print(s1.__dict__)


