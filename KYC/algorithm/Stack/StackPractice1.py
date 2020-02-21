# 수식적 풀이
ans = [1,3]
T = int(input())
for t in range(1,T+1):
    N = int(input())
    if N // 10 > len(ans):
        for a in range(len(ans),N//10):
                if a % 2 == 0:
                    ans.append(ans[-1]*2-1)
                else:
                    ans.append(ans[-1]*2+1)
        print("#{} {}".format(t,ans[-1]))
    else:
        print("{} {}".format(t,ans[N//10 -1]))

