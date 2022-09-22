t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    s=0
    for _ in range(l,r+1):
        if _%10==2 or _%10==3 or _%10==9:
            s+=1
    print(s)