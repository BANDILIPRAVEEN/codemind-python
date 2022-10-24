a=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=0
for i in range(k):
    s+=arr[i]
print(s)