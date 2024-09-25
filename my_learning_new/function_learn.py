# # def addiction(a,b):
# #     return a+b
# #
# #
# # c=addiction(5,8)
# # print(c)
#
#
#
# def dual(a,b,c,d):
#     return a+b,c*d
#
# e,f=dual(7,8,9,4)
# print(e)
# print(f)

# def odd_even(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# # odd_even(8)

# lambda function

# f = lambda a,b,c,d: (a+b, c*d)
#
# res = f(8,4,5,3)
#
# print(res)


# def is_even(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# g = is_even
#
# j = map(lambda x: x % 2 == 0, [2,3,4,5,6,7])
# print(j)
# print(list(j))
#
# print(g(67))


class BinarySearch:

    def __init__(self, key, l):
        self.key = key
        self.l = l

    def search(self):
        if not self.l:
            return -1
        low = 0
        high = len(self.l) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.l[mid] == self.key:
                return mid
            elif self.l[mid] < self.key:
                low = mid + 1
            else:
                high = mid - 1
        return -1

key = 7
b1 = BinarySearch(key, [1, 3, 5, 7, 9, 11,12,13,14,15])
print(b1)
result = b1.search()
if result != -1:
    print(f"Element {key} found at index {result}.")
else:
    print(f"Element {key} not found in the list.")

b1
