def solution(progresses,speeds):
    ans = []
    while len(progresses) != 0:
        progresses = [progresses[i]+ speeds[i] for i in range(len(progresses))]
        stop = -1
        for i in range(len(progresses)):
            if progresses[i] < 100:
                stop = i
                break
        if stop == -1:
            ans.append(len(progresses))
            break
        elif stop != -1 and stop != 0:
            ans.append(stop)
            progresses = progresses[stop:]
            speeds = speeds[stop:]
        
    return ans

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses,speeds))