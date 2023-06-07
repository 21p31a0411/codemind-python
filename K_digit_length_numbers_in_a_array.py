n,kk=map(int,input().split())
l=list(map(int,input().split()))
k=[]
for i in l:
    k.append(str(abs(i)))
    
c=0
for i in k:
    
    if len(i)==kk:
        c=c+1

print(c)