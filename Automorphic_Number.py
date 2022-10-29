n=int(input())
sqr=n*n
if sqr%10==n or sqr%100==n or sqr%1000==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")