class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Actor(Person):
    def __init__(self,name,age,film,awards):
        super().__init__(name,age)
        self.film=film
        self.awards=awards

class Bollywood(Actor):
    def __init__(self,name,age,film,awards):
        super().__init__(name,age,film,awards)

b1=Bollywood("RAHUL",34,"PK","ifa")
