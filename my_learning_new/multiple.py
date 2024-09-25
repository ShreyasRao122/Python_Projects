class Actor:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_name(self):
        print(self.name,self.age)
    # def talk(self):
    #     print("Iam a actor")


class Awards:
    def __init__(self,film):
        self.film=film

    def talk(self):
        print("I am awards")


class Bollywood(Actor,Awards):
    def __init__(self,name,age,film,songs):
        Actor.__init__(self, name,age)
        Awards.__init__(self, film)
        self.songs=songs


p1=Bollywood("aaa",22,"bbb","ccc")
p1.display_name()

p1.talk()

