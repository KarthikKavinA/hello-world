s=input()
v=ord(s[1])
l=list(s)
a=[]
rr=0
te=0
result=[]
for i in l:
    a.append(ord(i))
c=a.copy()
c.pop(0)
c.pop(0)
lll=len(c)
rs=0
for i in range(lll):
    if min(c)>v:
        rr=min(c)
        te=c.index(min(c))
        break
    else:
        temp=c.index(min(c))
        c.pop(temp)
        rs+=1

ll=a.copy()
ll.pop(1)
ll.insert(1,rr)
ll.append(v)
ll.pop(te+rs+2)   #initially 2 pop() is called.
rrr=ll[2:]
rrr.sort()
res=ll[0:2]
res.extend(rrr)
for i in res:
    result.append(chr(i))
sss="".join(result)
print(sss)
