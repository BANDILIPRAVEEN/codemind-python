t=int(input())
for i in range(t):
    n=int(input())
    prev_prime=n
    while True:
        fct_cnt=0
        for i in range(1,prev_prime+1):
            if prev_prime%i==0:
                fct_cnt+=1
        if fct_cnt==2:
            break
        prev_prime-=1
    nxt_prime=n
    while True:
        fct_cnt=0
        for i in range(1,nxt_prime+1):
            if nxt_prime%i==0:
                fct_cnt+=1
        if fct_cnt==2:
            break
        nxt_prime+=1
    if n-prev_prime<=nxt_prime-n:
        print(prev_prime)
    else:
        print(nxt_prime)