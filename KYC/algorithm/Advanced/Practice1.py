def trans(a):
    ans = ""
    while True:
        if a == 0:
            break
        q, r = divmod(a,2)
        ans = "{}".format(r) + ans
        a = q
        
    if len(ans) < 4:
        ans = "0"*(4-len(ans)) + ans
    return ans

def jinbub(S):
    global dic
    ans = ""
    for a in S:
        if a in dic.keys():
            ans += trans(dic.get(a))
        else:
            ans += trans(int(a))
    return ans
key = ["A","B","C","D","E","F"]
val = list(range(10,16))
dic = dict(zip(key,val))

T = int(input())
for t in range(1,T+1):
    N, S = list(input().split())
    print("#{} {}".format(t,jinbub(S)))