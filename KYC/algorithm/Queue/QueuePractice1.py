T = int(input())
for t in range(1,T+1):
    N, M = list(map(int, input().split()))
    question = list(input().split())
    buf = 0
    while M > 0:
        buf = question[0]
        for a in range(1,len(question)):
            question[a-1] = question[a]
        question[-1] = buf
        M -= 1
    print("#{} {}".format(t,question[0]))

# queue 모듈 사용 한 방식

import queue
T = int(input())
for t in range(1,T+1):
    N, M = list(map(int, input().split()))
    question = input()
    q = queue.Queue()
    for a in question.split(): #question 값을 queue에 집어 넣는 과정
        q.put(a)
    for b in range(M):
        mid = q.get()
        q.put(mid)
    print("#{} {}".format(t,q.get()))
        


