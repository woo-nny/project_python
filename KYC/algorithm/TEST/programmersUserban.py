def backtraking(u_id,b_id):
    if len(b_id) == 0:
        if lis not in check_list:
            input_list = lis.copy()
            check_list.append(input_list)
    else:
        for u in range(len(u_id)):  
            if lis[u] == False:          
                for b in range(len(b_id)):
                    check = False
                    if len(u_id[u]) == len(b_id[b]):
                        for i in range(len(u_id[u])):
                            if b_id[b][i] != '*' and b_id[b][i] != u_id[u][i]:
                                break
                            elif i == len(u_id[u])-1:
                                check = True
                    if check == True:
                        lis[u] = True
                        backtraking(u_id, b_id[:b]+b_id[b+1:])
                        lis[u] = False
                        

def solution(user_id,banned_id):
    global lis
    lis = [False] * len(user_id)
    if len(user_id) == len(banned_id):
        return 1
    backtraking(user_id,banned_id)
    return len(check_list)

check_list = []
lis = []
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id,banned_id))