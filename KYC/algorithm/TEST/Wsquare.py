def solution(W,H):
    s = [W,H]
    s.sort()
    if W == H or s[0] == 1:
        return W*H - s[1]
    else:
        for h in range(s[0],1,-1):
            if s[0] % h == 0 and s[1] % h== 0:
                return W * H - ((s[1]//h + s[0] // h -1) * (h))
    return W * H - (W + H -1)


#from math import gcd 를 이용해 최대공약수 구할 수 있음
print(solution(8,12))