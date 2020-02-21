from sys import stdin
T = int(stdin.readline())
for t in range(1,T+1):
    N = int(stdin.readline())
    ai = sorted(list(map(int, stdin.readline().split())))
    ans = ""
    for a in range(0,len(ai)):
        if a % 2 == 0:
            ans += " "+str(ai.pop(-1))
        else :
            ans += " "+str(ai.pop(0))
    print("#{}{}".format(t,ans))