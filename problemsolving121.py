# a=12345
# b=0
# while a!=0:
#     b=b+a%10
#
#     a=a//10
# print(b)
# from middle_element_of_list import mid_index


# a=5
# b=6
# c=a
# a=b
# b=c
# print(a)
# print(b)
# a,b=b,a
# print(a)
# print(b)
#
# a="mom"
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("Not palindrome")

# def sqr(x):
#     i = 1
#     while i * i <= x:
#         i += 1
#     return i - 1
# res = sqr(42)
# print(res)

# def last_occ(l,x):
#     for i in reversed(range(0,len(l))):
#         if l[i]==x:
#             return i
#     return -1
# l=[2,4,5,7,7,8]
# x=7
# result = last_occ(l,x)
# print(f'The last occurrence of {x} is at index: {result}')

#
# def first_occurance(hig,low,x,l):
#     if low>hig:
#         return -1
#     mid=(hig+low)//2
#     if x>l[mid]:
#         return first_occurance(low=mid+1,hig=hig,x=x,l=l)
#     elif x<l[mid]:
#         return first_occurance(hig=mid-1,low=0,x=x,l=l)
#     else:
#         if mid==0 or l[mid]!=l[mid-1]:
#             return mid
#         else:
#             return (first_occurance(hig=mid-1,low=low,x=x,l=l))
#
















#
# def last_occc(hig,low,k,l):
#     if low>hig:
#         return -1
#     mid=(low + hig)//2
#     if l[mid]>k:
#         return last_occc(hig=mid-1,low=low,k=k,l=l)
#     elif l[mid]<k:
#         return last_occc(low=mid+1,hig=hig,k=k,l=l)
#     else:
#         if len(l)-1 == mid or l[mid]!=l[mid+1]:
#             return mid
#         return last_occc(low=mid+1,hig=hig,k=k,l=l)
# l=[1,1,1,2,2,2,3,3,3]
# k=2
# print(last_occc(hig=len(l)-1,low=0,k=k,l=l))

#
# def count_occ(l,k):
#     cout=0
#     start=False
#
#     for i in l:
#         if i==k:
#             start=True
#             cout=cout+1
#         if start==True and k!=i:
#             break
#     print(cout)
# l=[1,1,1,2,2,2,2,3,3,3,3]
# k=2
# count_occ(l=l,k=k)




#
# def first_occurance(hig,low,x,l):
#     if low>hig:
#         return -1
#     mid=(hig+low)//2
#     if x>l[mid]:
#         return first_occurance(low=mid+1,hig=hig,x=x,l=l)
#     elif x<l[mid]:
#         return first_occurance(hig=mid-1,low=0,x=x,l=l)
#     else:
#         if mid==0 or l[mid]!=l[mid-1]:
#             return mid
#         else:
#             return (first_occurance(hig=mid-1,low=low,x=x,l=l))
#
# def last_occc(hig,low,k,l):
#     if low>hig:
#         return -1
#     mid=(low + hig)//2
#     if l[mid]>k:
#         return last_occc(hig=mid-1,low=low,k=k,l=l)
#     elif l[mid]<k:
#         return last_occc(low=mid+1,hig=hig,k=k,l=l)
#     else:
#         if len(l)-1 == mid or l[mid]!=l[mid+1]:
#             return mid
#         return last_occc(low=mid+1,hig=hig,k=k,l=l)
#
# def count_occ(k,l):
#     first=first_occurance(hig=len(l)-1,low=0,x=k,l=l)
#     if first==-1:
#         return 0
#     last=last_occc(hig=len(l)-1,low=0,k=k,l=l)
#     return last-first+1
# l=[1,1,1,1,2,2,2,2,2]
# k=2
# print(count_occ(k,l))

#
# def sqroot(hig,low,x,ans=-1):
#     if low>hig:
#         return ans
#     mid=(low+hig)//2
#     sqr=mid*mid
#     if sqr==x:
#         return mid
#     elif sqr>x:
#         hig=mid-1
#         return sqroot(hig=hig,low=low,x=x,ans=ans)
#     else:
#         low=mid+1
#         return sqroot(hig=hig,low=low,x=x,ans=mid)
# print(sqroot(hig=24,low=1,x=24))

# a = [[2,4,5], [8,6,9]]
# if len(a)>0:
#     elem_len=len(a[0])
#     sum =[0]*elem_len
#     for i in a:
#         for j in range(elem_len):
#             sum[j]=sum[j]+i[j]
#     print(sum)



d = [{"name":"kiran", "age":28, "status": True},
     {"name":"shreyas", "age":28, "status": False},
     {"name":"varun", "age":27, "status": True}]
for i in d:
    if i["status"]==True:
        print(i)

