def diference(n):
    product=1
    sum=0
    while n:
        r=n%10
        product*=r
        sum+=r
        n=n//10
    print(abs(product-sum))
n=int(input())
diference(n)