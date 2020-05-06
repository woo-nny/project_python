def solution(routes):
    routes.sort(key = lambda x : x[0])
    start = -30001
    cnt = 0
    while True:
        cnt += 1
        length = len(routes)
        end = 30000
        for i in range(length):
            route1,route2 = routes.pop(0)
            if route1 > start:
                routes.append([route1,route2])
                if end > route2:
                    end = route2
        if len(routes) == 0:
            break

        start = end
        
    return cnt-1
            



routes = [[-20, 15]]


print(solution(routes))
