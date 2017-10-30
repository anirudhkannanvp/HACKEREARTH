n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
maximum=max(b)+1
ans=0
for i in range(n1):
    if(a[i]<maximum):
        ans+=maximum-a[i]
print(ans)