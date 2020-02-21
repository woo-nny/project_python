T = int(input())

for T in range(T):
    N,M = map(int,input().split())
    C = list(map(int,input().split()))
    Queue = []

    for i in range(N):
        Queue.append([C[i], i]) #치즈 , 피자 번호
    #print(Queue)
    i = 0
    while len(Queue)!=1:
        Queue[0][0] //= 2 #한바퀴 돌고 녹지 않은 치즈 양 반으로 줄어듬

        if Queue[0][0] == 0: #녹지 않은 치즈양이 0
            if N + i < M: #남은 피자가 있으면 추가
                Queue.pop(0)
                Queue.append([C[N+i], N+i])
                i+=1
            elif N+i >= M: #남은 피자가 있으면 pop
                Queue.pop(0)
        else: #녹지 않은 양이 있으면 다음 칸으로 넘어감
            Queue.append(Queue.pop(0)) 

    print("#{} {}".format(T+1,Queue[0][1]+1))