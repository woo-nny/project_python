def backtracking(row,now_MIN,count):
    global N
    global MIN
    if MIN >= now_MIN and count >= N :
        MIN = now_MIN
        return
    elif MIN <= now_MIN:
        return
    elif count == N-1 and check_list[0] == True:
        return
    else:
        for column in range(0,N):
            if check_list[column] == False and row != column:
                check_list[column] = True
                backtracking(column,now_MIN + question[row][column],count+1)
                check_list[column] = False

T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = []
    for n in range(N):
        question.append(list(map(int, input().split())))
    MIN = 5000
    check_list = [False]*N
    backtracking(0,0,0)
    print("#{} {}".format(t,MIN))