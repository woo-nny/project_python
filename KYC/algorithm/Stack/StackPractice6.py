# def solution(lis,a,b,stack,check):
#     addlis = [[a+1,b],[a-1,b],[a,b+1],[a,b-1]]
#     for i in addlis:
#         if 0 <= i[0] < len(lis) and 0<= i[1] < len(lis):
#             if lis[i[0]][i[1]] != 1 and stack.count(i) == 0:
#                 stack.append(i)
#                 check.append(lis[i[0]][i[1]])
#                 solution(lis,i[0],i[1],stack,check)

# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     lis = []
#     for a in range(N):
#         lis.append(list(map(int, input().strip())))
    
#     stack = []
#     check = []
#     for a in range(0,len(lis)):
#         for b in range(0,len(lis)):
#             if lis[a][b] == 2:
#                 stack.append([a,b])
#                 check.append(lis[a][b])
#                 break
#     solution(lis,stack[-1][0],stack[-1][1],stack,check)
#     if check.count(3) == 1:
#         print("{} {}".format(t,1))
#     else:
#         print("{} {}".format(t,0))
            
def dfs(lis,stack):
    while True:
        a, b = stack.pop(-1)
        addlis = [[a+1,b],[a-1,b],[a,b+1],[a,b-1]]
        for i in addlis:
            if 0 <= i[0] < len(lis) and 0<= i[1] < len(lis):
                if lis[i[0]][i[1]] == 0:
                    lis[i[0]][i[1]] = 4
                    stack.append(i)
                elif lis[i[0]][i[1]] == 3:
                    return 1
        if len(stack) == 0:
            break
    return 0

T = int(input())
for t in range(1,T+1):
    N = int(input())
    lis = []
    for a in range(N):
        lis.append(list(map(int, input().strip())))
    stack = []
    for j in range(0,len(lis)):
        for k in range(0,len(lis)):
            if lis[j][k] == 2:
                stack.append([j,k])
    print("#{} {}".format(t,dfs(lis,stack)))

                
