n=int(input())
a=list(map(int,input().split()))
b=[]
che=[]
che1=[]
for i in range(10000000):
    che.append(0)
    che1.append(0)
for i in range(n-1,-1,-1):
    b.append(a[i])
for i in range(n):
    if(che1[a[i]]==0):
        che1[a[i]]=i
    che[a[i]]=i
che1[a[0]]=0
#print("che",che)
#print("che1",che1)
ans=-1
n1=n
for i in range(n):
    ans=max(ans,abs(che1[i]-che[i]))
print(ans+1)