n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
avg=s/n
print('{:.2f}'.format(avg))