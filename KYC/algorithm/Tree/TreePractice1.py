#dfs를 이용한 풀이
T = int(input())
for t in range(1,T+1):
    E, N = list(map(int, input().split()))
    question = list(map(int, input().split()))
    lis = list()
    for a in range(0,len(question),2):
        lis.append([question[a],question[a+1]])
    stack = [N]
    length = len(lis)
    cnt = 0
    while len(stack) != 0:
        G = stack.pop(-1)
        for i in range(length):
            a = lis.pop(0)
            stack.append(a[1]) if a[0] == G else lis.append(a)
        length = len(lis)
        print(lis)
        cnt += 1

    print("#{} {}".format(t,cnt))