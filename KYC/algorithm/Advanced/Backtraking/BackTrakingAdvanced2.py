def backtraking(row,now_sum):
    global Min
    global N
    if row >= N:
        if Min > now_sum:
            Min = now_sum
            return
        else:
            return
    elif now_sum > Min:
        return
    else:
        for i in range(N):
            if check_box[i] is False:
                check_box[i] = True
                backtraking(row+1,now_sum + question[row][i])
                check_box[i] = False


T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = []
    for _ in range(N):
        question.append(list(map(int, input().split())))
    Min = N*100
    check_box = [False]*N
    backtraking(0,0)
    print("#{} {}".format(t,Min))