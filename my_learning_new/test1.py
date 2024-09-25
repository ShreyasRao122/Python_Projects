# r = [1, 2]
# a = iter(r)
# print(a)
# b = next(a)
# print(b)
# c = next(a)
# print(c)
# for x in r:
#print(x)

s = "1212134553244"*15
unique=set()
freq={}
print(s)
for i in s:
    u=int(i)
    unique.add(u)
    if u not in freq:
        freq[u]=1
    else:
        freq[u]+=1

print(unique)
print(freq)

# for i in unique:
#     print(s.count(str(i)),i)





