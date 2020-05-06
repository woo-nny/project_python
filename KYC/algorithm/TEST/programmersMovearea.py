def solution(land,height):
    answer = 0
    check_box = []
    N = len(land)
    for i in range(N):
        check_box.append([False]*N)
    ladder_point = [[0,0,0]]
    same_area = []
    count = 0
    while count < N**2:
        if len(same_area) == 0:
            l_N = len(ladder_point)
            for i in range(l_N):
                _y,_x,_add = ladder_point.pop(0)
                if check_box[_y][_x] == False:
                    ladder_point.append([_y,_x,_add])
            y,x,add = ladder_point.pop(0)
            answer += add
            check_box[y][x] = True
            same_area.append([y,x])
            count += 1
        else:
            dyx = [[1,0],[-1,0],[0,1],[0,-1]]
            y,x=same_area.pop()
            for dy,dx in dyx:
                if -1 < x+dx < N and -1< y+dy< N and check_box[y+dy][x+dx] == False:
                    fee = abs(land[y][x]-land[y+dy][x+dx])
                    if fee <= height:
                        check_box[y+dy][x+dx] = True
                        same_area.append([y+dy,x+dx])
                        count += 1
                    else:
                        ladder_point
    
    return answer


land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = 3

print(solution(land,height))
