n=int(input())
arr=list(map(int,input().split()))
first=0
for i in range(n):
    if arr[i]%2==1:
        break
    first+=arr[i]
print(first)