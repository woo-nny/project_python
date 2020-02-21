from sys import stdin
T = int(stdin.readline())
for test in range(1,T+1):
    N = int(stdin.readline())
    graph = []
    for a in range(0,10):
        graph.append([])
        for b in range(0,10):
            graph[a].append(0)
    for num in range(0,N):
        a = list(map(int, stdin.readline().split()))
        if a[-1] == 1:
            for b in range(a[0],a[2]+1):
                for c in range(a[1],a[3]+1):
                    graph[b][c] += 1
        else:
            for b in range(a[0],a[2]+1):
                for c in range(a[1],a[3]+1):
                    graph[b][c] += 100
    cnt = 0
    for a in graph:
        for b in a:
            if b >100:
                cnt += 1
    print("#{} {}",format(test,cnt))
    

            