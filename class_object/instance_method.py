class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hi",self.name)
        print("You have:",self.marks,"marks")
    def grade(self):
        if self.marks>75:
            print('You have Distinction')
        elif self.marks>60:
            print('You have First class')
        elif self.marks>40:
            print('You have Pass Class')
        else:
            print('You are failed')
n=int(input('Enter count of student:'))
for i in range(n):
    name=input("Enter Name:")
    marks=int(input("Enter Marks:"))
    S1=Student(name,marks)
    S1.display()
    S1.grade()
    print("\n")
