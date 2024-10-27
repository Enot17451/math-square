from random import *

class Square:

    def __init__(self):
        self.a = randint(2,7)
        self.b = randint(2,7)

    def __str__(self):
        return f"√{self.a*(self.b**2)}                                                                      {self.b}√{self.a}"

n = 20
for x in range(n):
    s = Square()
    print(s)
