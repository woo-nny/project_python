T = int(input())
for t in range(1,T+1):
    N , M, G = list(map(int, input().split()))
    lis = [0]*N
    for i in range(M):
        j, n = list(map(int, input().split()))
        lis[j-1] = n
    for i in range(len(lis)-1,-1,-1):
        P = (i+1)//2 - 1
        if lis[P] == 0:
            if len(lis) > (P+1)*2:
                lis[P] = lis[(P+1)*2 - 1] + lis[(P+1)*2]
            else:
                lis[P] = lis[(P+1)*2 - 1]
    print("#{} {}".format(t, lis[G-1]))