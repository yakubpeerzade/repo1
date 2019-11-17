class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def Count(cls):
        print('Count of object:',Test.count)

T1=[]

for i in range(5):
    T1.append(Test())
Test.Count()
