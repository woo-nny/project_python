T = int(input())
for t in range(1,T+1):
    N = float(input())
    ans = ""
    cnt = 1
    while N != 0 and cnt < 14:
        if N - 2**(-1*cnt) >= 0:
            ans += "1"
            N -= 2**(-1*cnt)
        else:
            ans += "0"
        cnt += 1
    if cnt <= 13:
        print("#{} {}".format(t,ans))
    else:
        print("#{} overflow".format(t))