# x=55 # global
# def fun():
#     x=30 # local
#     print(x)
#
# fun()
# print(x)


# class A:
#     country = "ind"
#
#     def __init__(self, age):
#         self.age = age
#
#
# a = A(55)
# b = A(88)
#
# A.country = "India"
#
#
# print(a.age)


class Car:
    counter = 0  # class variable

    def __init__(self, name):
        self.name = name  # instance variable


a = []
for x in range(10):
    c = Car("BMW" + str(x))
    a.append(c)
    Car.counter += 1
print(a)
