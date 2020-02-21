T = int(input())

for T in range(T):
    N , M = map(int,input().split())
    num = list(map(int,input().split()))
    #계산
    #a=M%N
    #print("#{} {}".format(T+1,num[a]))
    
    #Queue
    for i in range(M):
        num.append(num.pop(0)) # 처음 숫자를 빼고 바로 추가 함
    print("#{} {}".format(T+1,num[0]))

        