# 가장쉬운 백트래킹
# def find_min_dist(x,y,now_dist):
#     global Min
#     global length
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     if now_dist > Min :
#         return
#     elif x == y == length-1 :
#         if now_dist < Min:
#             Min = now_dist
#         return
#     else:
#         for i in range(4):
#             new_x, new_y = x+dx[i], y+dy[i]
#             if 0 <= new_x < length and 0 <= new_y < length and check_metrix[new_x][new_y] == False:
#                 check_metrix[new_x][new_y] = True
#                 new_now_dist = now_dist + 1
#                 if metrix[new_x][new_y] > metrix[x][y]:
#                     new_now_dist += (metrix[new_x][new_y] - metrix[x][y])
#                 find_min_dist(new_x,new_y,new_now_dist)
#                 check_metrix[new_x][new_y] = False

# T = int(input())
# for t in range(1,T+1):
#     length = int(input())
#     metrix = []
#     check_metrix = []
#     for _ in range(length):
#         metrix.append(list(map(int, input().split())))
#         check_metrix.append([False]*(length))
#     Min = 1000
#     find_min_dist(0,0,0)
#     print("#{} {}".format(t,Min))

# 우선순위 큐를 이용한 다익스트라 알고리즘
import heapq
def Dijkstra():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    check_q = []
    start = [0,0,0]
    heapq.heappush(check_q,start)
    while True:
        key,x,y = heapq.heappop(check_q)
        if x == y == length-1:
            break
        for i in range(4):
            new_x, new_y = x+dx[i],y+dy[i]
            if 0<= new_x < length and 0 <= new_y < length:

                add = (metrix[new_x][new_y] - metrix[x][y]
                if metrix[new_x][new_y] > metrix[x][y] else 0) + 1
                if distance[x][y] + add < distance[new_x][new_y]:
                    distance[new_x][new_y] = distance[x][y] + add
                    heapq.heappush(check_q,[distance[new_x][new_y],new_x,new_y])
    
    return distance[length-1][length-1]
T = int(input())
for t in range(1,T+1):
    length = int(input())
    metrix = []
    distance = []
    for _ in range(length):
        metrix.append(list(map(int, input().split())))
        distance.append([float('inf')]*length)
    distance[0][0] = 0
    print("#{} {}".format(t,Dijkstra()))

