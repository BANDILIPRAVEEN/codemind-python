n=int(input())
sum1=0
product=1
while n>0:
    r=n%10
    sum1+=r
    product*=r
    n=n//10
if sum1==product:
    print('Spy Number')
else:
    print('Not Spy Number')