def backtrack(a, k, input):
    global maxcandidates
    c = [0] * maxcandidates
    if k == input:
        process_solution(a,k)
    else :
        k += 1
        ncandidates = construct_candidates(a,k,input,c)
        for i in range(ncandidates):#최초 k가 0 일때    이후 K 가 1이되어       k가 3이될때까지 backtrack이 실행되며
            a[k] = c[i]             #a[0] true일때      true가 a[1]에 저장     값이 쌓이게되고
            backtrack(a,k,input)    #backtrack실행      #backtrack이 실행    process_solution이 진행
                                    #위의 과정이 한번 끝나면 a=[true*3,false*n-3]이고 이때 for문은 아직 false일때를 남겨놨으므로
                                    #다음 과정에서 a = [true*2 , false*n-2]가 된다
                                    #그리고 이 이전에 k = 2 일때 for문의 c[0] = true인 경우만 했으므로
                                    #다시 c[1] = false인 경우를 실행하고 k=3이되어 여기서 또다시 true,false인경우를 실행하는방식
                                    #즉 a = [true,false,true,....]실행 후 a = [true,false,false,....]
                                    #결국 for문이 가장 늦게 실행되는 a[0] = c[1]의 경우의 c[1],c[1]이 될때 까지 실행되고 종료
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2
def process_solution(a, k):
    print("(",end = "")
    for i in range(k+1):
        if a[i]:
            print(i,end="")
    print(")")

maxcandidates = 100
a = [0]*maxcandidates
backtrack(a,2,4)