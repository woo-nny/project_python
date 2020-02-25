def merge(problem,ans):
    if len(problem) <= 1:
        return problem, ans
    else:
        left, ans_1 = merge(problem[:len(problem)//2], ans)
        right, ans_2 = merge(problem[len(problem)//2:len(problem)], ans)
        if left[-1] > right[-1]:
            ans = ans_1 + ans_2 + 1
        else:
            ans = ans_1 + ans_2
        sort_list = []
        length = len(left)+len(right)
        while len(sort_list) != length:
            if len(left) != 0 and len(right) !=0:
                L, R = left[0], right[0]
                if L <= R:
                    sort_list.append(left.pop(0))
                else:
                    sort_list.append(right.pop(0))
            elif len(left) == 0:
                sort_list.append(right.pop(0))
            elif len(right) == 0:
                sort_list.append(left.pop(0))
        return sort_list, ans

T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = list(map(int,input().split()))
    a, b = merge(question, 0)
    print("#{} {} {}".format(t, a[N//2], b))

