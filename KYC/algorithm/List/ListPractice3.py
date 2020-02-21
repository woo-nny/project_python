import sys
T = int(sys.stdin.readline())
for a in range(1,T+1):
    K, N, M = map(int, sys.stdin.readline().split())
    M_num = list(map(int, sys.stdin.readline().split()))
    lis = list(range(0,N+1))
    for b in M_num:
        lis[b] = 1
    mid = 0
    cnt = 0
    while mid < N-K:
        mid_sum = 0
        for c in range(mid+K,mid,-1):
            if lis[c] == 1:
                mid = c
                cnt += 1
                mid_sum += 1
                break
        if mid_sum == 0:
            cnt = 0
            break
    print("#{} {}".format(a, cnt))
