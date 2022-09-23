a=int(input())
b=int(input())
pfs_a=0
for i in range(1,a):
    if a%i==0:
        pfs_a+=i
pfs_b=0
for c in range(1,b):
    if b%c==0:
        pfs_b+=c
if pfs_a==b and pfs_b==a:
    print('Amicable')
else:
    print('Not Amicable')