def solution(v):
    v.sort()
    x = v[2][0]+v[0][0] -v[1][0]
    v.sort(key = lambda x :x[1])
    y = v[2][1]+v[0][1] - v[1][1]
    return [x,y]



sqare = [[1, 4], [3, 4], [3, 10]]
print(solution(sqare))