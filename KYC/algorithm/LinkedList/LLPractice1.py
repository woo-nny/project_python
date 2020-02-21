T = int(input())
for t in range(1,T+1):
    N,M,L = list(map(int, input().split()))
    prob = list(map(int, input().split()))
    for m in range(M):
        ind, item = list(map(int, input().split()))
        prob.insert(ind, item)
    print("#{} {}".format(t,prob[L]))