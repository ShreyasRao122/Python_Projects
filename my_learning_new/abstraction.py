from abc import ABC,abstractmethod
class Phone(ABC):
    def __init__(self, n):
        self.n = n
    def calling(self):
        print("Calling")

    @abstractmethod
    def texting(self):
        pass

    @abstractmethod
    def camera(self):
        pass

class Nokia(Phone):
    def texting(self):
        print("Texting")

    def camera(self):
        pass


n=Nokia()
n.texting()
n.calling()