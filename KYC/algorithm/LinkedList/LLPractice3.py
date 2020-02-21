T = int(input())
for t in range(1,T+1):
    N, M, K = list(map(int,input().split()))
    lis = list(map(int,input().split()))
    c = 1
    s = 0
    while c <= K:
        s = s+M
        if s < len(lis):
            lis.insert(s,lis[s] + lis[s-1])
        elif s == len(lis):
            lis.append(lis[s-1] + lis[0])
        else:
            s = s-len(lis)
            lis.insert(s, lis[s] + lis[s-1])
        c += 1
    print("#{}".format(t),end = "")
    if len(lis) < 10:
        for a in range(len(lis)):
            print(" {}".format(lis.pop(-1)),end = "")
    else:
        for a in range(10):
            print(" {}".format(lis.pop(-1)),end = "")
    print()