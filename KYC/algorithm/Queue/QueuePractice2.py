import queue

def checkpoint(a,b,question):
    check_lis = []
    check_list = [[a+1,b],[a-1,b],[a,b+1],[a,b-1]]
    for i in check_list:
        if -1<i[0]<len(question) and -1<i[1]<len(question):
            if question[i[0]][i[1]] == 0:
                check_lis.append([i[0],i[1]])
                question[i[0]][i[1]] = 1
            elif question[i[0]][i[1]] == 3:
                check_lis.append([3])
    return check_lis

T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = []
    for a in range(0,N):
        question.append(list(map(int,input().strip())))
    q = queue.Queue()
    for a in range(len(question)): # 2가 시작하는 좌표를찾는다.
        for b in range(len(question[a])):
            if question[a][b] == 2:
                q.put([[a,b]])
                break
        if q.qsize() == 1:
            break
    # cnt는 얼마만큼 떨어져 있느냐이다. 여기서 체크할 때, 3을 찾는 과정이 포함되어 있으므로 2를 빼준다.
    cnt = -2 
    checker = False
    while q.qsize() > 0 and checker == False:
        mid_lis = []
        for a in q.get():
            if a == [3]:
                checker = True
                break
            else:
                mid_lis += checkpoint(a[0],a[1],question)
        if mid_lis != []:
            q.put(mid_lis)
        cnt += 1
    if checker == False:
        print("#{} {}".format(t,0))
    else :
        print("#{} {}".format(t,cnt))
