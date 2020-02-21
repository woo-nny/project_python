def search_MIN(now_min,X,Y,count,length):
    global MIN
    
    if MIN <= now_min:
        return
    elif count == length*2 and MIN >= now_min:
        MIN = now_min
        return
    else:
        for x,y in [[X+1,Y],[X,Y+1]]:
            if x <= length and y <= length:
                #여기서 now_min값을 밖으로 빼서 계산하면 for구문을 2번째 돌때 앞의 숫자도 더해져 버린다.
                search_MIN(now_min + problem[x][y],x,y,count+1,length)



T = int(input())
for t in range(1,T+1):
    N = int(input())
    problem = []
    for n in range(N):
        problem.append(list(map(int,input().split())))
    MIN = 2500
    search_MIN(problem[0][0], 0, 0, 0, N-1)
    print("#{} {}".format(t,MIN))
