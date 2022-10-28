n=int(input())
sqr=n*n
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
sqr_rev=rev*rev
rev2=0
while sqr_rev:
    r2=sqr_rev%10
    rev2=rev2*10+r2
    sqr_rev=sqr_rev//10
if sqr==rev2:
    print("True")
else:
    print("False")
    