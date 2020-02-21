TEST = int(input())
for T in range(1,TEST+1):
    N, M = list(map(int, input().split()))
    text = []
    for a in range(0,N):
        text.append(input())
    ans = ""
    for a in range(0,N): # 가로일 경우나 세로일 경우나 결국 N번의 행또는 열을 돌아야 한다
        for b in range(0,N-M+1): # 가로일 경우, 행의 제한을 세로일 경우 가로에 제한을 두기위한 구문.
            check1 = True
            check2 = True
            mid = 0 #while구문안에서 반으로 나눠서 확인을 해야하고, 이때 mid값을 기준으로 사용한다.
            while mid <= M // 2: # 만약 mid값이 절반보다 작아지면 같은 작업은 반복하므로 더 이상 진행하지 않음
                if text[a][b+mid] != text[a][b+M-1-mid]: # 가로줄 확인
                    check1 = False # 확인해서 틀리면 false
                if text[b+mid][a] != text[b+M-1-mid][a]: # 세로줄 확인
                    check2 = False
                mid += 1
            if (check1 == True) or (check2 == True): # 최종적으로 True라는건 결국 맞는 값이 있었다는 소리.
                if check1 == True:
                    ans = text[a][b:b+M]
                else:
                    for c in range(0,M):
                        ans += text[b+c][a]
                break # 더이상 2번재 for 구문을 실행하지 않음
        if (check1 == True) or (check2 == True):
            break # 맞는 값이 있다면 1번째 for 구문을 실행하지 않음.
    print("#{} {}".format(T,ans))
