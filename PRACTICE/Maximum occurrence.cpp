#include <bits/stdc++.h>
using namespace std;
typedef ll long long int;

int main()
{
    ll A[256];
for(ll i = 0; i < 256; i++){
    A[i] = 0;
}
string S;
getline(cin, S);
ll index;
for(ll i = 0; i < S.size(); i++){
    index = S.at(i);
    A[index] = A[index] + 1;
}
ll max = A[0];
ll idx = 0;
for(ll i = 1; i < 256; i++){
if(A[i] > max){
    max = A[i];
    idx = i;
}
}
cout<<(char)idx<<" "<<max<<"\n";
return 0;
}