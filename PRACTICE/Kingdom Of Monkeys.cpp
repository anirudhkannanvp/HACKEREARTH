#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
 
int main()
{
ios_base::sync_with_stdio(false);
cin.tie(0);
ll t=0;
cin>>t;
while(t--)
{
ll n=0,m=0,x=0,y=0;
cin>>n>>m;
list<ll> *adj=new list<ll>[n+1];
list<ll> stack;	
for(ll i=0;i<m;i++)
{
cin>>x>>y;
adj[x].push_back(y);
adj[y].push_back(x);
}
ll a[n+1],b[n+1]; a[0]=0; b[0]=0;
for(ll i=1;i<=n;i++)
{
cin>>a[i];
}
bool visited[n+1];
for(ll j=0;j<=n;j++)
visited[j]=false;
ll sum=0,max=0; int j=0;
    for(ll i=1;i<=n;i++) 
{
ll p=i;
visited[i]=true;
stack.push_back(i);
while(!stack.empty())
{
ll temp=stack.front();
p=temp;
sum+=a[p];
stack.pop_front();
list<ll>::iterator it;
for(it=adj[p].begin();it!=adj[p].end();it++)
{
if(!visited[*it])
{
visited[*it]=true;
stack.push_back(*it);
}
}
}
b[j]=sum;
j++;
sum=0;
}
max=b[0];
for(ll i=1;i<j;i++)
{
if(max<b[i])
max=b[i];
}
cout<<max<<endl;
 
}
return 0;
}