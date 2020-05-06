def solution(t):
    for r in range(len(t)-2,-1,-1):
        for c in range(len(t[r])):
            t[r][c] = max(t[r][c]+t[r+1][c],t[r][c]+t[r+1][c+1])
    return t[0][0]

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))

# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])