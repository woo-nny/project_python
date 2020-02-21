def DelReduplication(str):
    res = []
    for a in str:
        if len(res) == 0 or a != res[-1]:
            res.append(a)
        else:
            res.pop(-1)
    return len(res) if len(str) == len(res) else DelReduplication(res)
T = int(input())
for t in range(1,T+1):
    str = list(input())
    print("#{} {}".format(t,DelReduplication(str)))