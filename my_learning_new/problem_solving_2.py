# a=list(range(1,11))
# a=a*3
# print(a)
# b=set(a)
# print(b)
# c=(1,2,3)
# print(c)
# d=tuple(range(1,4))
# print(d)
# f=tuple("shhh")
# print(f)
# for i in "ghj":
#     print(i)
# g=1,2,3
# print(g)

a=set()
for i in range(1,11):
    i=i**2
    a.add(i)
print(a)
for i in range(1,101):
    # g=i**2
    if i**2 in a:
        print(i)