t=int(input())
while(t):
    t-=1
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if(k==0):
        s=0
        for i in range(n):
            if(a[i]>=0):
                s+=a[i]
        print(s)
    else:
        dp=[0]*n
        if(a[0]<0):
            dp[0]=0
        for i in range(n):
            if((i-k-1)<0):
                dp[i]=max(a[i],dp[i-1]);
            else:
                dp[i]=max(dp[i],a[i],max(dp[i-1], dp[i-k-1]+a[i]))
        print(dp[n-1])