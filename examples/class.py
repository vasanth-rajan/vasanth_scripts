class Vasanth(object):
    # global varible 
    d = 10
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(self.d)
    
    def add(self,e, f):
        self.c = self.a + self.b
        self.c = e + f
        return self.c 

    def subtract(self):
        self.c = self.d - self.a
        return self.c




aa = Vasanth(5,6)
print(aa.a, aa.b, aa.d)

bb = aa.add(6,7)
print(bb)

print(aa.subtract())
