T = int(input())
for t in range(1,T+1):
    V, E = list(map(int, input().split()))
    checklist = []
    for e in range(0,E):
        checklist.append(list(map(int, input().split())))
    start, end = list(map(int, input().split()))
    ans = 0
    anslis = []
    for a in checklist: # 최초 시작할 노드 정해줌.
        if a[0] == start:
            anslis.append(a[1])
    check = True
    while check:
        mid = []
        for a in checklist:#스택의 top위치의 원소를 이용해 자식이 있는지 없는지 판단
            if a[0] == anslis[-1]:
                mid.append(a[1])#자식이 있다면 중간값에 추가해주고
        if end in mid:#중간값에 찾는 값이 있다면, 최종적으로 목표에 도달 할 수있으므로 종료
            ans = 1
            break
        anslis.pop(-1)#그렇지 않다면 pop을하고
        anslis += mid#push를 해준다
        if len(anslis) == 0:
            ans = 0
            break
    print("#{} {}".format(t,ans))