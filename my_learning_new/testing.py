a = {
  "kiran": 5,
  "shreyas": [2, 5],
  None: 88,
}


print(a)
print(a.keys())
print(a.values())
print(a.items())

a["kiran"]=88
a.update([("ddd",89)])
a.update({"poiu":89})
print(a)



