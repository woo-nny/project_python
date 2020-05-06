def make_graph(data1,data2):
    x = now_head[data1]
    y = now_head[data2]
    if x != y:
        x, y = [x,y] if x < y else [y,x]
        for i in range(len(now_head)):
            if now_head[i] == y:
                now_head[i] = x


T = int(input())
for t in range(1,T+1):
    N, M = list(map(int,input().split()))
    question = list(map(int,input().split()))
    now_head = list(range(N+1))
    for i in range(0,len(question),2):
        make_graph([question[i],question[i+1]])
    print("#{} {}".format(t,len(set(now_head))-1))