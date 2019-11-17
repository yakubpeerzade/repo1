class stud:
    '''Class created by yaqoob'''
    def __init__(self,name,age,marks):
        self.name='Yakub'
        self.age=23
        self.marks=80
        
    def talk(self):
        print("Hello I am:",self.name)
        print("My age is:",self.age)
        print("My marks are:",self.marks)
        
s1=stud('Yakub',23,90)
s1.talk()
