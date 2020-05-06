from collections import deque
T = int(input())
for t in range(1,T+1):
    calculate_list = [1,-1,"*2",-10]
    N, M = list(map(int,input().split()))

    # 시간을 단축 할 수 있는 방법. 중복 숫자를 제거하는 경우 효율적이다.
    num_list = [0] * 1000001
    num_list[N] = N
    #----------------------------
    que = deque()
    que.append([N,0])
    breaker = True
    while breaker:
        i,cnt = que.popleft()
        for j in calculate_list:
            mid = i + j if j != "*2" else i * 2
            if mid == M:
                ans = cnt + 1
                breaker= False
                break
            elif 0 < mid < 1000000 and num_list[mid] == 0:
                que.append([mid,cnt+1])
                num_list[mid] = mid
    print("#{} {}".format(t,ans))
