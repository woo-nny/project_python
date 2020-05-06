T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = {}
    for i in range(N): # 최초 값을 받을때 부터 쓸모 있을 값만 받아서 검사 갯수를 줄인다.
        start, end = list(map(int, input().split()))
        if end not in question.keys():
            question[end] = start
        else:
            if question[end] < start:
                question[end] = start
    now_list = list(zip(question.keys(), question.values()))
    save_list = now_list.copy()
    cnt = 0
    length = len(now_list)
    while length > 0:#가능성있는 모든 다리를 건너는 방식.
        for i in range(length):
            end, start = now_list.pop(0)
            for m_end, m_start in save_list:
                if m_end <= start:
                    now_list.append([m_end,m_start])
        length = len(now_list)
        cnt += 1
    print("#{} {}".format(t, cnt))