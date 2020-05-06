def solution(n, costs):
    result = 0
    costs.sort(key = lambda x : x[2])
    parents_list = [i for i in range(n)]
    for i in range(len(costs)):
        x,y = costs[i][0],costs[i][1]
        x_p = union_set(x,parents_list)
        y_p = union_set(y,parents_list)
        if x_p < y_p:
            parents_list[y] = x_p
            parents_list[y_p] = x_p
            result += costs[i][2]
        elif x_p > y_p:
            parents_list[x] = y_p
            parents_list[x_p] = y_p
            result += costs[i][2]
    return result

def union_set(x,parents_list):
    if parents_list[x] == x:
        return x
    else:
        return union_set(parents_list[x], parents_list)

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(5,costs))