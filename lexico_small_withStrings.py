n=input()
l=list(n)
ll=l.copy()
v=l[1]
t=l[2:]               #slicing from 3rd element.
j=0
te=0
tt=0
s=''
for i in range(len(t)):
    if min(t)>v:
        tt=min(t)
        te=t.index(min(t))
        break
    else:
        j+=1
        temp=t.index(min(t))
        t.pop(temp)
ll.pop(1)
ll.insert(1,tt)
ll.append(v)          #sliced value (2)+te+j
ll.pop(2+te+j)              
res=sorted(ll[2:])
r=ll[0:2]
r.extend(res)
s="".join(r)
print(s)
