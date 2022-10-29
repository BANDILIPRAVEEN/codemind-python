n=int(input())
sqr=n**2
len_mod=pow(10,len(str(n)))
if sqr%len_mod==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")