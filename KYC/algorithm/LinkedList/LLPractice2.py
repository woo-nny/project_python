T = int(input())
for t in range(1,T+1):
    N,M = list(map(int, input().split()))
    res = []
    prob = list(map(int, input().split()))
    res += prob
    for m in range(M-1):
        check = len(res)
        prob = list(map(int, input().split()))
        for a in range(len(res)):
            if res[a] > prob[0]:
                res = res[:a] + prob + res[a:]
                # for b in range(len(prob)):
                #     res.insert(a,prob.pop(-1))
                break
        if len(res) == check:
            res += prob

    print("#"+str(t),end = "")
    for a in range(-1,-11,-1):
        print(" {}".format(res[a]),end = "")
    print()

