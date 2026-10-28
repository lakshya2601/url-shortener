class Test:
    def __init__(self, b):
        self.a = 2
        self.b = b
    
    def add(self, c):
        return self.a + self.b + c

    def result(self):
        return self.add(10)

obj = Test(5)
print(obj.add(7))
print(obj.result())

#access specifier

class Phone:
    def __init__(self):
        self.brand = "samsung"

p = Phone()
print(p.brand)
p.brand = "Apple"
print(p.brand)


#self.price     # public
#self._price    # protected
#self.__price   # private