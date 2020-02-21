import queue as qu

T = int(input())
for t in range(1,T+1):
    V, E = list(map(int, input().split()))
    Bg_que = qu.Queue() #거치지 않은 모든 길을 저장하는 큐
    Que = qu.Queue() # 1다리를 건널경우(단계) 생길 모든 시작점을 저장해 놓은 큐
    for i in range(E):
        Bg_que.put(list(map(int,input().split()))) 
    S, G = list(map(int, input().split()))
    check = True
    Que.put(S)

    # while구문을 한번 돌때마다 1다리씩 건너는 형식이 된다. 즉 cnt는 몇 단계를 거쳤느냐를 기록
    cnt = 0
    while check:
        #Que의 크기는 중간 중간 변하니 변수로 미리 빼준다.
        Que_size = Que.qsize()
        for i in range(0,Que_size):
            s = Que.get() # 한 단계에 해당하는 시작점을 하나씩 꺼낸다.
            # Bg_que의 크기는 중간에 변하므로 변수로 빼준다.
            num = Bg_que.qsize()
            # 시작하는 숫자가 A[0] 일수도 A[1]일 수도 있으니 모든 경우를 작성한다.
            for a in range(0,num):
                A = Bg_que.get() # 확인할 원소를 꺼낸다.
                if A[0] == s and A[1] != G:
                    Que.put(A[1]) # 위의 경우 아직 G에 도달 못했으므로 시작점을 Que에 저장
                elif A[1] == s and A[0] != G:
                    Que.put(A[0]) # 위의 경우 아직 G에 도달 못했으므로 시작점을 Que에 저장
                elif (A[0] == s and A[1] == G) or (A[1] == s and A[0] == G):
                    check = False # 위의 경우 G에 도달 했으므로 while을 끝내기위해 check 바꿈.
                else:
                    Bg_que.put(A) # 해당하는 길이 아니므로 원소를 다시 큐에 넣어준다.
        # 2중 for 구문을 전부 돌았다는 것은 Que 한번을 모두 돌았고 1단계를 거친 것이므로 +1을 해준다.
        cnt += 1
        # 만약 Que에 원소가 없다면 모든 경우를 다했거나, 더 이상 연결되는 고리가 없다는 것이므로 종료
        if Que.qsize() == 0:
            break

    if check == False:
        print("#{} {}".format(t, cnt))
    else:
        print("#{} {}".format(t, 0))