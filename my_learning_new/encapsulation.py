
class Person:
    def __init__(self,name,age, height):
        self.name=name
        self._age=age
        self.__height = height



    def disp(self):
        print(self.name, self._age, self.__height)


    def disply_height(self):
        print(self.__height)


    def modify_height(self,new_height, pin):
        if pin ==1111:
            self.__height=new_height
        else:
            print("Invalid Pin")



class D(Person):
    def walk(self):
        print(self._age)



p1=Person("SHREYAS",29, 88)
p2=Person("KIRAN",28, 66)

d = D("hi", 22, 77)

print(p1.__height)
print(p1.name)
p1.name="SHREYAS RAO"
print(p1.name)
p1.disply_height()
p1.modify_height(66,1111)
p1.disply_height()


