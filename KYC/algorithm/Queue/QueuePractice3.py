import queue
T = int(input())
for t in range(1,T+1):
    N,M = list(map(int, input().split()))

    question = list(map(int,input().split()))

    q1 = queue.Queue() #전체 피자
    q2 = queue.Queue() #화덕속 피자
    for a in range(len(question)): #전체 피자에 순서대로 번호를 매겨 줌.
        q1.put([question[a],a+1])
    
    for a in range(N): #최초 N개의 피자를 화덕에 넣어준다.
        q2.put(q1.get())

    while q2.qsize() > 1: #최종적으로 남는 하나를 빼고 모두가 사라질때 까지 시행한다.
        a,b = q2.get()
        a = a//2 # 1바퀴돌때 반이 되므로 결국 이 피자를 볼 때, 반이 되는 것과 같은 상황이다.
        if a != 0:
            q2.put([a,b])
        else:
            if q1.qsize() != 0:
                q2.put(q1.get())

    print("#{} {}".format(t,q2.get()[1]))