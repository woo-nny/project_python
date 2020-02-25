Test = int(input())
for test in range(1,Test+1):
    N, M = list(map(int, input().split()))
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort()
    T.sort()
    ans = 0
    while len(T) !=0 and len(W) != 0:
        t = T.pop(-1)
        w = W.pop(-1)
        if w > t:
            T.append(t)
        else:
            ans += w
    print("#{} {}".format(test,ans))