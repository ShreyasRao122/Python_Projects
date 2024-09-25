#
# class Person:
#     def __init__(self,name,age, height):
#         self.name=name
#         self._age=age
#         self.__height = height
#
#
#
#     def disp(self):
#         print(self.name, self._age, self.__height)
#
#
#     def disply_height(self):
#         print(self.__height)
#
#
#     def modify_height(self,new_height, pin):
#         if pin ==1111:
#             self.__height=new_height
#         else:
#             print("Invalid Pin")
#
#
#
# class D(Person):
#     def walk(self):
#         print(self._age)
#
#
#
# p1=Person("SHREYAS",29, 88)
# p2=Person("KIRAN",28, 66)
#
# d = D("hi", 22, 77)
#
#
# print(p1.name)
# p1.name="SHREYAS RAO"
# print(p1.name)
# p1.disply_height()
# p1.modify_height(66,1111)
# p1.disply_height()
#
#
# class Person:
#     def __init__(self,name,age, height):
#         self.name=name
#         self.age=age
#         self.height = height
#
# p1=Person("SHREYAS",29, 88)
#
# print(p1.name)
# print(p1.age)
# print(p1.height)
#
# a=[10,20,30,45,55,70]
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even,odd)
# from copy import deepcopy
from middle_element_of_list import mid_index


# a=[10,20,30,1,2,3,4]
# x=5
# op=[]
# for i in a:
#     if i<x:
#         op.append(i)
# print(op)

#
# for x in range(5):
#     if x > 3:
#         break
# else:
#     print(55)
#
# def getmaxx(l: list[int]):
#     if not l:
#         return None
#     # if len(l) < 1:
#     #     return None
#     else:
#         maxx=l[0]
#         for x in range(1,len(l)):
#             if maxx < l[x]:
#                 maxx=l[x]
#             # maxx = max(maxx, l[x])
#         return maxx
#
# def secmax(l):
#     if not l:
#         return None
#     larg=getmaxx(l)
#     slarg=None
#     for x in l:
#         if x!=larg:
#             if slarg==None:
#                slarg=x
#             else:
#                 slarg=max(slarg,x)
#     return slarg
# k=[9,2,7,4,7]
# res=secmax(k)
# print(res)


# def getmaxx(l: list[int]):
#     if not l:
#         return None
#     maxx = l[0]
#     for x in range(1, len(l)):
#         if maxx < l[x]:
#             maxx = l[x]
#     return maxx
#
# def secmax(l):
#     if not l:
#         return None
#     larg = getmaxx(l)
#     slarg = None
#     for x in l:
#         if x != larg:
#             if slarg is None or x > slarg:
#                 slarg = x
#     return slarg
#
# k = [9, 2, 7, 4, 7]
# res = secmax(k)
# print(res)
# def sorlist(l):
#     i=1
#     while i<len(l):
#         if l[i]<l[i-1]:
#             return False
#         i=i+1
#     return True
# l=[1,2,3]
# if sorlist(l):
#     print("YES")
# else:
#     print("No")

# flag = True
#
# while flag:
#     print("*")
#     flag = bool(int(input("enter 0 to exit other number to continue: \n")))
#     print(flag)




# a = [1,2,3,4,5,6]
# for x in range(len(a)-1, -1, -1):
#     if a[x] == 5 or a[x]==3:
#         continue
#     print(a[x])

#
# a = [1,2,3,4,5,6,7,8,9]
# s = 0
# for x in range(2, len(a), 3):
#     s += a[x]
# print(s)

#
# a=[10,20,30,50,40,30]
# l=0
# h=len(a)-1
# while l<=h:
#     a[l],a[h]=a[h],a[l]
#     l=l+1
#     h=h-1
# print(a)

# def leftrot(l):
#     n=len(l)
#     x=l[0]
#     for i in range(1,n):
#         l[i-1]=l[i]
#     l[n-1]=x
#     return l
# k=[1,2,3,4,5]
# res=leftrot(k)
# print(res)

# def dublic(arry,n):
#     temp=[0]*n
#     temp[0]=arry[0]
#     res=1
#     for i in range(1,n):
#         if temp[res-1]!=arry[i]:
#             temp[res]=arry[i]
#             res+=1
#     for i in range(0,res):
#         arry[i]=temp[i]
#     # print(arry)
#     return arry
# a=[6,8,8,9,9,10]
# ress=dublic(a,len(a))
# print(a)
#
# def dub(arry,n):
#     res=1
#     for i in range(1,n):
#         if(arry[res-1]!=arry[i]):
#             arry[res]=arry[i]
#             res+=1
#     return res
# a=[1,2,2,3,4,4]
# r= dub(a,len(a))
#
# for _ in range(len(a)-1, r-1,-1):
#     a.pop()
# print(a)
#
# a=[2,3,4,5,6,8,9,22,33,44,99,88,66,55]
# i,f,s=1,True,0
# while i<len(a):
#     s=s+a[i]
#     if f==True:
#         i=i+4
#         f=False
#     else:
#         i=i+2
#         f=True
# print(s)

# a=[3,4,5,6,7,8, 11, 45]
# b = deepcopy(a)
# for i in b:
#     if i < 10:
#         print(i)
#         a.remove(i)
#
# print(a)

#
# def fun(k):
#     if k==0:
#         return
#     print("GFG")
#     fun(k-1)
# fun(1)

# def fun1ton(n):
#     if n==0:
#         return
#     fun1ton(n-1)
#     print(n)
#     fun1ton(n-1)
# fun1ton(3)
# def fun1(n):
#     if n==0:
#         return 0
#     k=n%10
#     n=n//10
#     return k+fun1(n)
# res=fun1(1234)
# print(res)
#
# def is_palindrome(a):
#     if len(a)==0 or len(a)==1:
#         return True
#     if a[0]==a[len(a)-1]:
#         return is_palindrome(a[1:len(a)-1])
#
#     else:
#         return False
# print(is_palindrome("aiai"))

# def fun1(bignum,smallnum):
#     if smallnum>bignum:
#         print("Invalid number")
#         return 0
#     if bignum==smallnum:
#         return smallnum
#     return bignum + fun1(bignum-1,smallnum)
# print(fun1(23,25))



# def binary_search(key, l):
#     if not l:
#         return -1
#     low=0
#     high= len(l) - 1
#     while low<=high:
#         mid=(low+high) // 2
#         if l[mid] == key:
#             return mid
#         elif l[mid] < key:
#             low=mid + 1
#         else:
#             high=mid - 1
#     return -1
# key=7
# result=binary_search(key, [1, 3, 5, 7, 9, 11])
# if result != -1:
#     print(f"Element {key} found at index {result}.")
# else:
#     print(f"Element {key} not found in the list.")
#
# def binary_search_recursive(key, l, low, high):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if l[mid] == key:
#         return mid
#     elif l[mid] > key:
#         return binary_search_recursive(key, l, low, mid - 1)
#     else:
#         return binary_search_recursive(key, l, mid + 1, high)
#
# arr= [1, 3, 5, 7, 9, 11]
# key=7
# result=binary_search_recursive(key=key, l=arr, low=0, high=len(arr) - 1)
# if result!=-1:
#     print(f"Element {key} found at index {result}.")
# else:
#     print(f"Element {key} not found in the list.")

# def first_occ(l,x):
#     for i in range(0,len(l)):
#         if l[i]==x:
#             return i
#     return -1
# l=[2, 4, 5, 7, 8]
# x=8
# result = first_occ(l,x)
# print(f'The first occurrence of {x} is at index: {result}')

# def last_occ(l,x):
#     for i in reversed(range(0,len(l))):
#         if l[i]==x:
#             return i
#     return -1
# l=[2,4,5,7,7,8]
# x=7
# result = last_occ(l,x)
# print(f'The last occurrence of {x} is at index: {result}')

# def sqr(x):
#     i = 1
#     while i * i <= x:
#         i += 1
#     return i - 1
# res = sqr(41)
# print(res)




# class PalindromeChecker:
#     def __init__(self, text):
#         self.text = text
#     def is_palindrome(self):
#         return self._check_palindrome(self.text)
#
#     def _check_palindrome(self, a):
#         if len(a) == 0 or len(a) == 1:
#             return True
#         if a[0] == a[len(a)-1]:
#             return self._check_palindrome(a[1:len(a)-1])
#         else:
#             return False
# checker = PalindromeChecker("aiaia")
# print(checker.is_palindrome())

