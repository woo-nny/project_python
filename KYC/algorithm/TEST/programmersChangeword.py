def solution(begin,target,words):
    answer = 0
    check_list = [False]*len(words)
    backtraking(begin,target,words,0,check_list)
    if Min == 99999:
        return 0
    else:
        return Min

def backtraking(begin,target,words,count,check_list):
    global Min
    if begin == target and count < Min:
        Min = count
        return
    elif count >= Min:
        return
    else:
        for i in range(len(words)):
            if check_list[i] == False and sum([x!=y for x, y in zip(words[i], begin)]) == 1:
                # c = 0
                # for j in range(len(begin)):
                #     if words[i][j] != begin[j]:
                #         c += 1
                #     if c > 1:
                #         c = 2
                #         break
                # if c == 1:
                check_list[i] = True
                backtraking(words[i],target,words,count+1,check_list)
                check_list[i] = False


Min = 99999
begin = "hit"
target = "cog"
words = ["hot",'dit','dig','lit','log','cog']
# target = 'hhh'
# words = ['hhh','hht']

print(solution(begin,target,words))
