
# T = int(input())
# for t in range(1,T+1):
#     N, M, L = list(map(int, input().split()))
#     lis = list(map(int,input().split()))
#     for i in range(M):
#         stage = list(input().split())
#         if stage[0] == "I":
#             lis.insert(int(stage[1]),int(stage[2]))
#         elif stage[0] == "D":
#             lis.pop(int(stage[1]))
#         else:
#             lis[int(stage[1])] = int(stage[2])
#     if len(lis) > L:
#         print("#{} {}".format(t,lis[L]))
#     else:
#         print("#{} {}".format(t,-1))