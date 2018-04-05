import re
a=list(input())
convert = lambda text: int(text) if text.isdigit() else text 
ascii_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
a.sort(key=ascii_key)
a2=list(set(a))
n=len(a)
n1=len(a2)
cou=[0]*n1
for i in range(n):
   t=a2.index(a[i])
   cou[t]+=1
t1=cou[0]
ans=0
for i in range(1,n1):
    if(cou[i]>t1):
        ans=i
        t1=cou[i]
print(a2[ans],max(cou))