T = int(input())
for t in range(1,T+1):
    str1 = input()
    str2 = sorted(input())
    str1Set = set(str1) # 후보군의 중복없이 만들어준다.
    zeros = [0]*len(str1Set)# 딕셔너리에 들어가기 위해 후보군의 초기값을 설정해준다.
    dic = dict(zip(str1Set,zeros)) # 위의 2개를 key값으로 str1set, values값으로 zeros로하여 딕셔너리화 한다.
    for a in str2:# for 구문을 이용해 str2와
        if a in dic.keys(): # key값을 비교하고
            dic[a] += 1 # 키값과 같은 글자가 나온경우 value의 값을 +1 해준다.
    ans = [[k, v] for k, v in dic.items() if dic[k] == max(dic.values())] # 최종적으로 딕셔너리를 확인해 최대값구함.
    print("#{} {} {}".format(t, ans[0][0], ans[0][1]))
    