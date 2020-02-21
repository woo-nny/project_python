# def rcp2(a,b,ind_list,c):
#     if a == b:
#         rcp_stack.append(a)
#         ind_stack.append(c[0])
#     elif (a == 2 and b == 1) or (a==3 and b == 2) or (a==1 and b==3):
#         rcp_stack.append(a)
#         ind_stack.append(c[0])
#     else:
#         rcp_stack.append(b)
#         ind_stack.append(ind_list[0])

# def rcp(question,ind_list):
#     a,b = question[0],question[1]
#     if a == b:
#         rcp_stack.append(a)
#         ind_stack.append(ind_list[0])
#     elif (a == 2 and b == 1) or (a==3 and b == 2) or (a==1 and b==3):
#         rcp_stack.append(a)
#         ind_stack.append(ind_list[0])
#     else:
#         rcp_stack.append(b)
#         ind_stack.append(ind_list[1])

def rcp(check, question): # 각대진의 승부를 기록하는 코드,가위바위보에서 진사람은 False로 만들어준다.
    if len(check) == 2:
        a,b = question[check[0]],question[check[1]]
        if a == b:
            question[check[1]] = False
        elif (a == 2 and b == 1) or (a==3 and b == 2) or (a==1 and b==3):
            question[check[1]] = False
        else:
            question[check[0]] = False
def solution(ind_stack,TM): # 전체 토너먼트 대진을 다 만들어주는 코드
    while True:
        a = TM[-1]
        mid = []
        for i in a:
            if (i[1] - i[0]) > 1:
                mid.append([i[0],(i[0]+i[1])//2])
                mid.append([(i[0]+i[1])//2+1,i[1]])
        TM.append(mid)
        if TM[-1] == []:
            TM.pop(-1)
            break
    return TM

def solution2(TM,question):#대진이 다 만들어진 후, 대진을 이용해 각 대진들의 승부를 보게하는 코드
    ans = 0
    while True:
        a = TM.pop(-1)
        for i in a:
            if i[0] != i[1]:
                check = []
                for b in range(i[0],i[1]+1):
                    if question[b] != False:
                        check.append(b)
                rcp(check,question)
        if len(TM) == 0:
            for i in range(0,len(question)):
                if question[i] != False:
                    ans = i
                    break
            break
    return ans       


T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = list(map(int,input().split()))
    TM = [[[0,len(question)-1]]]
    ind_stack = list(map(int,list(range(0,len(question)))))
    solution(ind_stack,TM)
    print("#{} {}".format(t,1+solution2(TM, question)))

