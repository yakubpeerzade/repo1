class Test:
    x=90

    def __init__(self):
        self.y=10
        self.z=20
t=Test()
print(t.__dict__)
print(Test.x)
Test.x=555
t1=Test()
print(t1.__dict__)
print(Test.x)
