n=int(input())
arr=list(map(int,input().split()))
b=sum(arr)
while b%n!=0:
    n-=1
print(n)