'''import sys

for line in sys.stdin:
    print(line[0])
'''
import re
n=int(input())

cl=[]
pl=[]
pll=[]

c=int(input())
for i in range(c):
    cl.append(list(map(str,input().split())))
    
    
p=int(input())
for i in range(p):
    tt=input()
    pl.append(re.findall('[0-9]',tt))

#print(pl)   
    
for i in pl:
    s=0
    for j in i:
        s=s+int(cl[int(j)-1][2])
    pll.append(s)

#print(pll)  
    
i=0
to=0
while(i<c):
    if n*int(cl[i][1])<=int(cl[i][2]):
        to=to+int(cl[i][2])
    else:
        to=to+int(cl[i][2])
        ttt=n*int(cl[i][1])
        while True:
            to=to+pll[i]
            temp=ttt-int(cl[i][2])
            ttt=ttt-int(cl[i][2])
            if temp==int(cl[i][1]):
                break
    i=i+1
            
            
print(to) 
