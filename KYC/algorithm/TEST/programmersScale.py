def solution(weight):
    weight.sort()
    A = 0
    for i in range(0,len(weight)):
        if A+1 < weight[i]:
            break
        A += weight[i]
    return A+1
weight = [3, 1, 6, 2, 7, 30, 1]
print(solution(weight))