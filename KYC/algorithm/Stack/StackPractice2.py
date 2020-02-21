T = int(input())
for t in range(1,T+1):
    question = input()
    checklis = []
    ans = 1
    for a in question:
        if a =="(" or a == "{" or a== "[":
            checklis.append(a)
        elif a == ")":
            if len(checklis) == 0 or checklis.pop(-1) != "(":
                ans = 0
                break
        elif a=="}":
            if len(checklis) == 0 or checklis.pop(-1) != "{":
                ans = 0
                break
        elif a == "]":
            if len(checklis) == 0 or checklis.pop(-1) != "[":
                ans = 0
                break
    if len(checklis) != 0:
        ans = 0
    print("#{} {}".format(t,ans))