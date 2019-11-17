class Employee:
    def __init__(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
    def display(self):
        print("Employee name:",self.name)
        print("Employee Id:",self.eid)
        print("Employee Salary:",self.sal)
class Test:
    def empl(emp):
        emp.name='Jack'
em=Employee('yakub',2,10000)
em.display()
Test.empl(em)
em.display()
