class student:
   def det(self):
       self.name=input("Enter Name:")
       self.rno=int(input("Enter rollo:"))
       self.marks=int(input("Enter Marks:"))
       
   def display(self):
       print("Student Name:",self.name)
       print("Roll Number:",self.rno)
       print("Marks obtained:",self.marks)
s1=student()
print("Enter Student Details")
s1.det()
print("Student info")
s1.display()
