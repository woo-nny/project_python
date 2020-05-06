def solution(key,lock):
    
    N = len(lock)
    M = len(key)
    
    lock_numb = 0
    for r in lock:
        lock_numb += r.count(0)
    cnt = 1

    while cnt <= 4:
        
        
        key_pattern = make_pattern(1,key)    
        for r in range(N-1,-N,-1):
            for c in range(N-1,-N,-1):
                check_num,check = 0,True
                for c_k in key_pattern:
                    new_r = c_k[0] - r
                    new_c = c_k[1] - c
                    if 0 <= new_r < N and 0 <= new_c < N:
                        if lock[new_r][new_c] == 0:
                            check_num += 1
                        else:
                            check = False
                            break
                if check_num == lock_numb and check == True:
                    return True
                
        c_key = []
        for i in range(M):
            add_list = []
            for j in range(M-1,-1,-1):
                add_list.append(key[j][i])
            c_key.append(add_list)
        key = c_key

        cnt += 1

    
    return False

def make_pattern(find,list):
    L = len(list)
    pattern = []
    for r in range(L):
        for c in range(L):
            if list[r][c] == find:
                pattern.append([r,c])
    return pattern


lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

print(solution(key,lock))