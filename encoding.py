import numpy as np

def func(n):
    s1=0
    a=list(n)
    a.reverse()
    m=int(a[0])
    for i in range(1,len(a)):
        if(int(a[i])!=m):
            s1=s1+(m*(10**(i-1)))
            m=int(a[i])
    s1=s1+(int(a[-1])*(10**(len(a)-1)))
    return (s1)


T=int(input())
list1=[]
for j in range(T):
    NL,L=[(x) for x in input().split()]
    NR,R=[(x) for x in input().split()]
    s=0
    for i in range(int(L),int(R)+1):
        s=s+func(str(i))
    list1.append(s%(10**9+7))
    
for item in list1:
    print(item)