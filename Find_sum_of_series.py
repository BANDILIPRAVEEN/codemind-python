n=int(input())
s=0
for i in range(1,n+1):
    r=1/i
    s+=r
print('{:.2f}'.format(s))