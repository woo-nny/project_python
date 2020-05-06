def solution(n):
    answer = [0]
    for i in range(1,n):
        answer = answer + [0] + [0 if i == 1 else 1 for i in answer]
    return answer


print(solution(3))