from sys import stdin
T = int(stdin.readline())
for a in range(1,T+1):
    N, M = map(int, stdin.readline().split())
    lis = list(map(int, stdin.readline().split()))
    sumlis = [0,sum(lis[0:M])] # 최대값과 최소값을 넣을 공간
    for b in range(0,N-M+1): # M개씩 넣어서 나올 모든 숫자를 비교한다.
        c = sum(lis[b:b+M])
        if c > sumlis[0]:
            sumlis[0] = c
        elif c < sumlis[1]:
            sumlis[1] = c
    print("#{} {}".format(a,sumlis[0]-sumlis[1]))
