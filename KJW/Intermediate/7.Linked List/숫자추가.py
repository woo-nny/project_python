T = int(input())

for T in range(T):
    N,M,L = map(int,input().split())
    ans = list(map(int,input().split()))
    for M in range(M):
        a, b = map(int,input().split())
        ans.insert(a,b)
    res=ans[L]
    print("#{} {}".format(T+1,res))