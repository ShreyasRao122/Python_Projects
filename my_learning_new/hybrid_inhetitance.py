class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Actor(Person):
    def __init__(self,name,age,film,awards, height):
        super().__init__(name,age, height)
        self.film=film
        self.awards=awards


class Apperrance(Person):
    def __init__(self,name,age,height):
        super().__init__(name,age)
        self.height=height


class Person1(Actor, Apperrance):
    def __init__(self,name,age,film,awards,height,name1):
      super().__init__(name, age, film, awards, height)
      self.name1=name1

p1=Person1("SHREYAS",24,"pk","iff",6,"sss")




