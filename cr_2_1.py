#1 агрегация
class A:
    def __init__(self, a):
        self.a = a

class B:
    def __init__(self, b):
        self.b = b

a = A("Y")
b = B(a)

#2 компоизиция

class C:
    def __init__(self):
        pass

class D:
    def __init__(self):
        self.d = C()

d = D("jfd")
