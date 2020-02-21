def binary(start,end,purpose,cnt):
    center = (start + end)//2
    if center == purpose:
        return cnt
    else:
        if purpose > center:
            start = center + 1
            cnt += 1
            return binary(start, end, purpose,cnt)
        else:
            end = center - 1
            cnt += 1
            return binary(start, center, purpose,cnt)
            
T = int(input())
for t in range(1,T+1):
    P,A,B = map(int, input().split())
    Acnt = binary(1, P, A, 1)
    Bcnt = binary(1, P, B, 1)
    if Acnt > Bcnt:
        print("#{} {}".format(t,"A"))
    elif Acnt < Bcnt:
        print("#{} {}".format(t,"B"))
    else:
        print("#{} {}".format(t,"0"))