class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
    def talk(self):
        print("i am talking")

    def move(self):
        print("i am moving car")




c = Car("bmw", "xp")

print(c.brand)
print(c.model)
c.move()


