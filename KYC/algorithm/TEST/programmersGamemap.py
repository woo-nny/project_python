# 0은 벽이 있는 자리
def solution(maps):
    height = len(maps)
    width = len(maps[0])
    maps[0][0] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    start = [[1,0,0]]
    ans = -1
    while True:
        check = False
        c,h,w = start.pop(0)
        for i in range(4):
            new_h = h+dx[i]
            new_w = w+dy[i]
            if -1< new_h <height and -1 < new_w < width:
                if new_h == height-1 and new_w == width-1:
                    ans = c+1
                    check = True
                    break
                elif maps[new_h][new_w] == 1:
                    maps[new_h][new_w] = 0
                    start.append([c+1,new_h,new_w])
        if len(start) == 0 or check == True:
            break
    return ans

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps),maps)