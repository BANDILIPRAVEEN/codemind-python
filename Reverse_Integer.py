n=int(input())
t=abs(n)
rev=0
while t:
    r=t%10
    rev=rev*10+r
    t=t//10
if n<0:
    print(-rev)
else:
    print(rev)