

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Actor(Person):
    def __init__(self,name,age,film,awards):
        super().__init__(name,age)
        self.film=film
        self.awards=awards

class Apperrance(Person):
    def __init__(self,name,age,height):
        super().__init__(name,age)
        self.height=height


