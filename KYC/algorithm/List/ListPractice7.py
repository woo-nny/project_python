A = list(range(1,13))
lis = []
for a in range(1 << len(A)):
    num = 0
    sums = 0
    for b in range(len(A)):
        if a & (1 << b):
            num += 1
            sums += A[b]
    lis.append([num,sums])
sorted(lis)
T = int(input())
for test in range(1,T+1):
    N, K = map(int, input().split())
    cnt = 0
    for a in range(0,len(lis)):
        if lis[a] == [N, K]:
            cnt += 1
        elif lis[a][0] > N:
            break
    print("#{} {}".format(test,cnt))