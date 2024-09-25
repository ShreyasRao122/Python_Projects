# a=[1,2,3,3,4,5,66,66,8,9,2,2]
# print(a.count(66))
# b="I worK for sLK"
# print(b.count("o"))

# c=[1,1,1,2,2,2,2,3,3]
# d = []
# for x in set(c):
#     maxcount=c.count(x)
#     d.append(maxcount)
# print(max(d))
# # ***************************************
# c=[1,1,1,2,2,2,2,3,3]
# a={}
# for x in c:
#     if x in a:
#         a[x]+=1
#     else:
#         a[x]=1
# maxval=0
# most_rep_key=0
# for k,v in a.items():
#     if maxval < v:
#         maxval=v
#         most_rep_key=k
# print(f"Most repeated num={most_rep_key} Frequency={maxval}")

a = [1,2,3,4]

for x in range(len(a)):
    print(a[x])
    a.pop(x)
