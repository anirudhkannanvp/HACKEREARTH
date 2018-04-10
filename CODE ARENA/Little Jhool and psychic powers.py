a=list(input())
n=len(a)
c=1
sr=a[0]
st=0
for i in range(1,n):
    #print(c)
    if(c==6):
        st=1
        print("Sorry, sorry!")
        break
    if(a[i]==a[i-1] and a[i]==sr):
        c+=1
    else:
        sr=a[i]
        c=1
if(st==0):
    print("Good luck!")