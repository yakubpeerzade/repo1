class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks on {} legs'.format(name,Animal.legs))
Animal.walk('Cat')
Animal.walk('Tiger')
