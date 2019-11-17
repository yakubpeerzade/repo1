class P:
    def __init__(self):
        self.pname='Yakub'
        self.surname='Peerzade'
    def nam(self):
        print('parent name:',self.pname,self.surname)
class C(P):
    def __init__(self):
        super().__init__()
        self.name='Yamin'
    def cname(self):
        print('Child name:',self.name,self.pname,self.surname)
child=C()
child.cname()
child.nam()
