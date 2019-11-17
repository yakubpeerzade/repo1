class Mango:
    def __init__(self):
        self.count=300
    def get_mango_count(self):
        print('Count of mango=',self.count)
    def set_mango_count(self):
        self.count=int(input('Enter new mango count:'))
    
class Banana:
    def __init__(self):
        self.count=300
    def get_banana_count(self):
        print('Count of banana=',self.count)
    def set_banana_count(self):
        self.count=int(input('Enter banana new count:'))
class Fruit:
    def __init__(self):
        self.banana=Banana()
        self.mango=Mango()
    def get_fruit_count(self):
        self.banana.get_banana_count()
        self.mango.get_mango_count()
    def set_fruit_count(self):
        self.banana.set_banana_count()
        self.mango.set_mango_count()
f1=Fruit()
f1.get_fruit_count()
f1.set_fruit_count()
f1.get_fruit_count()
