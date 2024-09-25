class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def walk(self):
        print("I am walking")


class Actor(Person):
    def __init__(self,name,age,famous_film):
        super().__init__(name,age)
        self.famous_film=famous_film

    def acting(self):
        print("I am acting")


a=Actor("shreyas",23,"PK")
print(a.name)
print(a.age)
print(a.famous_film)
a.walk()
a.acting()


