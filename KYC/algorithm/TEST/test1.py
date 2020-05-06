def CB_positon(C,B):
    if C == B:
        return 0
    cnt = 0
    add = 0
    queue = [[[B,0]]]
    check_list = [float('inf')] * 200001
    while True:
        if len(queue) == 0 or C > 200000:
            return -1
        cnt_list = queue.pop(0)
        cnt += 1
        add += 1
        C += add
        new_list = []
        for i in range(0,len(cnt_list)):
            add_list= [-1,1,2]
            if cnt_list[i][1] == 1:
                add_list = [-1,2] 
            elif cnt_list[i][1] == -1:
                add_list = [1,2]
            for j in add_list:
                new = cnt_list[i][0] + j if j != 2 else cnt_list[i][0]*2
                if new == C:
                    return cnt
                elif 0 < new < 200001 and check_list[new] >= cnt:
                    check_list[new] = cnt
                    new_list.append([new,j])
                
        queue.append(new_list)

C, B = list(map(int, input().split()))
ans = CB_positon(C,B)
print(ans)
