def solution(n):
    global ans
    ans = 0
    dfs(n,[0,0],0)
    return ans
def dfs(n, using_number,result):
    global ans
    x,y = using_number
    if x == y == n and result == 0:
        ans +=1
    else:
        for i in [+1, -1]:
            if -1< result+i <= n and x <= n and y <= n:
                if i == +1:
                    dfs(n,[x+1,y],result+i)
                else:
                    dfs(n,[x,y+1],result+i)

ans = 0
solution(2)
print(ans)