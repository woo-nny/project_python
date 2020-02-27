def quick_sort(question):
    if len(question) == 1:
        return question
    elif len(question) == 0:
        return []
    else:
        pivot = question[0]
        i = 1
        j = len(question) - 1
        while i <= j:
            if question[i] >= pivot and question[j] <= pivot:
                question[i], question[j] = question[j], question[i]
                i += 1
                j -= 1
            elif question[i] < pivot and question[j] <= pivot:
                i += 1
            elif question[i] >= pivot and question[j] > pivot:
                j -= 1
            elif question[i] < pivot and question[j] > pivot:
                i += 1
                j -= 1
        question[0], question[j] = question[j], question[0]
        left = quick_sort(question[:j])
        right = quick_sort(question[j+1:])
        return left + [question[j]] + right

T = int(input())
for t in range(1,T+1):
    N = int(input())
    question = list(map(int, input().split()))
    ans = quick_sort(question)
    print("#{} {}".format(t,ans[N//2]))
