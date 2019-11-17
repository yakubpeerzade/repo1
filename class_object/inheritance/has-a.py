class Engine:
    a=90
    def __init__(self):
        self.b=30
    def m1(self):
        print('We are checking engine functionality')

class Car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print('**The Car**')
        print("The Engine functionality")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
car=Car()
car.m2()
