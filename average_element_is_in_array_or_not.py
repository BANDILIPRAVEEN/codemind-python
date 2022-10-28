n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
avg=s//n
if avg in arr:
    print("True")
else:
    print("False")