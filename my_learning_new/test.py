# def p(x,n):
#     return x**n
# print(p(5,6))
#
# def poww(i,j):
#     r=1
#     for _ in range(j):
#         r=r*i
#     print("lkkk")
#     return r
# print(poww(2,3))
#
# def poww(x,n):
#     if n==0:
#         return 1
#     temp=poww(x,n//2)
#     temp=temp*temp
#     if n%2==0:
#         return temp
#     else:
#         return temp*x
# print(poww(2,3))

def last_occc(hig,low,k,l):
    if low>=hig:
        return -1
    mid=(low + hig)//2
    if l[mid]>k:
        return last_occc(hig=mid-1,low=low,k=k,l=l)
    elif l[mid]<k:
        return last_occc(low=mid+1,hig=hig,k=k,l=l)
    else:
        if len(l)-1 == mid or l[mid]!=l[mid+1]:
            return mid
        return last_occc(low=mid+1,hig=hig,k=k,l=l)
l=[1,1,1,2,2,2,3,3,3]
k=2
print(last_occc(hig=len(l)-1,low=0,k=k,l=l))