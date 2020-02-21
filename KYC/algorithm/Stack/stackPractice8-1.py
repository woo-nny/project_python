def backtraking(row,check_column,mid_min):
    global MIN
    if mid_min > MIN:
        return
    if row == len(question):
        if MIN > mid_min:
            MIN = mid_min
            return

    for a in range(len(question)):
        if check_column[a] == False:
            check_column[a] = True
            backtraking(row+1,check_column,mid_min+question[row][a])
            check_column[a] = False


T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = []
    for a in range(N):
        question.append(list(map(int, input().split())))
    
    MIN = 1000
    check_column = [False] * len(question)

    backtraking(0,check_column,0)
    print("#{} {}".format(t,MIN))