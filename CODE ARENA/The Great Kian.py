n=int(input())
a=list(map(int,input().split()))
arr=[0,0,0]
for i in range(n):
    if(i%3==0):
        arr[0]+=a[i]
    elif(i%3==1):
        arr[1]+=a[i]
    else:
        arr[2]+=a[i]
print(*arr)