a={"names":45,"age":33}
a["name"] = "rahul"
a["age"] = 20
a[1] = 45
a[1] = 55
a[(1,2)] = 4
# a[{1,23}] = 6
# a[{12:34,45:56}] = 8
print(a)
for x in a.keys():
    print(x)
for y in a.values():
    print(y)
for z,w in a.items():

    print(z,w)

for x in a:
    if x in a:
        print(a[x])