Q = input()
T = input()
rT = list(reversed(T))
ind = 0
step = 0
while ind <= len(Q) - len(T):
    mid = 0
    for a in range(0,len(T)):
        step += 1
        if T[len(T)-1-a] != Q[len(T)-1-a+ind]:
            for b in range(0,len(rT)):
                step += 1
                mid = b
                if Q[len(T)-1-a+ind] == rT[b]:
                    break
            ind += mid
            break
    if mid == 0:
        print(step,ind,Q[ind:ind+len(T)])
        break
