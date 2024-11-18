# Composition

class A:
    def __init__(self, b):
        self.b = b

class B:
    def __init__(self, bread):
        pass

a = A("bruh")
b = B(b)

# Agregation

class C:
    def __init__(self, c):
        self.c = c(bread)

class D:
    def __init__(self, bread):
        pass

c = C("brub")
d = D(c)
