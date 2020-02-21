T = int(input())
for t in range(1,T+1):
    str1 = input()
    str2 = input()
    rstr1 = list(reversed(str1))
    a = len(str1)
    ans = 0
    
    check = True
    while a <= len(str2):
        if str1 == str2[a-len(str1):a]:
            ans = 1
            break
        else :
            if rstr1[0] == str2[a-1]:
                a += 1
            else:
                try:
                    a += rstr1.index(str2[a-1])
                except:
                    a += len(str1)
    print("#{} {}".format(t,ans))
