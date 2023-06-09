import math
n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if(i>=0):
        z=len(str(i))
        a.append(z)
    else:
        z=len(str(i))-1
        a.append(z)
print(*a)