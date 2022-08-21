class A:
    def falar(self):
        print('A')

class B(A):
    def falar(self):
        print('B')

class C(A):
    def falar(self):
        print('C')

class D(B,C):
    def falar(self):
        print('D')


d=D()
d.falar()