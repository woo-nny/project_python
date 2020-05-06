def Min_path(start):
    if start == N:
        return
    else:
        for i in node_info[start]:
            if i[1]+ distance[start] < distance[i[0]]:
                distance[i[0]] = i[1] + distance[start]
                new_start = i[0]
                Min_path(new_start)


T = int(input())
for t in range(1,T+1):
    N, E = list(map(int, input().split()))
    node_info = {}
    for _ in range(E):
        s, e, d = list(map(int, input().split()))
        if s not in node_info:
            node_info[s] = [[e,d]]
        else:
            node_info[s] += [[e,d]]
    distance = [float('inf') for _ in range(0,N+1)]
    distance[0] = 0
    Min_path(0)
    print("#{} {}".format(t,distance[N]))