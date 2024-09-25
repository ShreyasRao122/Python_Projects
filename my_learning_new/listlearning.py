a=list(range(1,10))
# for i in a:
#     if not (i>=20 and i<=30):
#         print(i)
#
# for i in a:
#     if i%5==0:
#         print(i)

b=5
# print(b in a)
#
# for i in a:
#     if b == i:
#         print("true")
#     else:
#         continue
#
# def find_num(key,num_list):
#     for i in num_list:
#         if key ==i:
#             return "Present"
#         else:
#             continue
#
#     return "Not present"
#
# ans = find_num(num_list=a,key=b)
# print(ans)


# def find_num(key,num_list):
#     is_not_present = True
#     for i in num_list:
#         if key == i:
#             print("Present")
#             is_not_present = False
#             break
#         else:
#             continue
#
#     if is_not_present:
#         print("Not present")
#
#
# find_num(num_list=a,key=b)

class Linear_search():
    def __init__(self,num_list):
        self.num_list=num_list

    def find_num(self,key):
        is_present=False
        for i in self.num_list:
            if key==i:
                is_present=True
                print("Present")
                break
        if not is_present:
            print("Not Present")


l=Linear_search(num_list=a)
l.find_num(b)





