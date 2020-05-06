def solution(N,stations,W):
    answer = 0
    block = []
    front = 1
    for station in stations:
        if 0 < station-W < N+1:
            block.append(station-W-front)
        front = station+W+1
    if stations[-1] + W < N:
        block.append(N-(stations[-1]+W))
    while len(block) != 0:
        n = block.pop(0)
        q,r = divmod(n,W*2+1)
        if r > 0:
            q += 1
        answer += q

    return answer

N = 16
stations = [9]
W = 2
print(solution(N,stations,W))
