n=int(input())
arr=list(map(int,input().split()))
first=0
second=0
for i in range(n):
    if i<n//2:
        first+=arr[i]
    else:
        second+=arr[i]
print(abs(first-second))