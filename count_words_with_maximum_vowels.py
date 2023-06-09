s=input()
l1=s.split()
v='aeiou'
l=[]
for i in l1:
    c=0
    for j in i:
        if j in v:
            c+=1
    l.append(c)
print(l.count(max(l)))