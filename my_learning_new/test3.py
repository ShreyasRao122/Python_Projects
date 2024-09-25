# a=[1,2,3,3,4,5,66,66,8,9,2,2]
# print(a.count(66))
# b="I worK for sLK"
# print(b.count("o"))

# c=[1,1,1,2,2,2,2,3,3]
# d = []
# for x in set(c):
#     maxcount=c.count(x)
#     d.append(maxcount)
# # print(max(d))
#
# a={"name":"Shreyas",
#    {"sss":"ddd"}:123
#    }
# print(a)
# def mysum(a,b):
#    c=a+b
#    return c
# d=mysum(5,6)
# print(d)

#
# 1
# 12
# 123

# a=9
# for i in range(1,a+1):
#    print()
#    for j in range(1,i+1):
#        print(j,end="")

# a="p"
# for i in range(ord("a"),ord(a)+1):
#    print()
#    for j in range(ord("a"),i+1):
#        print(chr(j),end="")
#
# a=[1,2,3,4,6,7,8,9]
# b=list(range(1,10))
# print(a)
# print(b)
# for i in b:
#    if i not in a:
#       print(i)
#
# a=[1,2,3,4,5,6,7,9]
# s=sum(a)
# print(s)
# actual_sum=(9*10)//2
# print(actual_sum)
# result=actual_sum-s
# print(result)

#      *
#    *   *
# *    *    *
#
# a=8
# for i in range(a): #n
#    print()
#    print((a-i-1)*" ",end="")
#    for j in range(i+1): # n
#       print("* ", end="")
#

# class WordsCount:
#    def char_count(self,input_str:str):
#       count_map={}
#       for i in input_str:
#          if i in count_map:
#             count_map[i]=count_map[i]+1
#          else:
#             count_map[i]=1
#       print(count_map)
# a=WordsCount()
# a.char_count("MY NAME")
# a.char_count([1,2,3,1,2,3,4,54,5,5,3,2,1,4])

# n=5
# for i in range(n):
#    for j in range(n-i):
#       print("* ",end="")
#    print()

# n=4
# for i in range(n,0,-1):
#    for k in range(i-1):
#       print(" ",end="")
#    for j in range(n-i+1):
#       print("*",end="")
#    print()
#
# n=5
# for i in range(n):
#     print(" "*i,end="")
#     for j in range(n-i):
#         print("* ", end="")
#     print()
#

# a=4
# for i in range(a): #n
#    print()
#    print((a-i-1)*" ",end="")
#    for j in range(i+1): # n
#       print("* ", end="")
# print()
# n=4
# for i in range(n):
#     print(" "*i,end="")
#     for j in range(n-i):
#         print("* ", end="")
#     print()



# def fun(num):
#
#    if num < 0:
#       return
#    print(num)
#    fun(num-1)
#    print("*"*num)
#
# fun(5)

#
# def sumn(num):
#     if num==0:
#         return num
#     return num + sumn(num - 1)
#
#
# v = sumn(5)
# print(v)

# def fib(num):
#     if num<0:
#         return 0
#     if num==0:
#         return 0
#     if num==1 or num==2:
#         return 1
#     newnum=fib(num-2) + fib(num-1)
#     return newnum
#
# num=5
#
# for x in range(num+1):
#     print(fib(x), end=" ")
#count the numbers
# n=555588
# count=0
# while n!=0:
#     n=n//10
#     count=count+1
# print(count)

# palindromw
# p="1212"
# a=p[::-1]
# if p==a:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# def ispal(n):
#     rev=0
#     temp=n
#     while temp!=0:
#         ld=temp%10
#         rev=rev*10+ld
#         temp=temp/10
#     return rev==n
# if __name__ == '__main__':
#     number=121
#     print(ispal(number))
#FACTORIAL
# n=5
# if n==0 or n==1:
#     print("1")
# else:
#     for i in n:
#         print(i)

#SUM OF N NATURAL NUMBERS
#
# n=6
# s=0
# s=n*(n+1)//2
# print(s)

#COUNT THE NUMBER OF DIGITS IN GIVEN NUMBER
# n=4567
# count=0
# while n!=0:
#    n=n//10
#    count=count+1
# print(count)


# FACTORIAL
# n=5
# if n==0 or n==1:
#     print("1")
# else:
#     for i in n:
#         print(i)

#LCM
# def lcm(a,b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     return a
# print(lcm(10,15))

# #PRIME NUMBER
# a=20
# if a==0:
#     print("not a prime number")
# else:
#     if

import test4

print(__name__)