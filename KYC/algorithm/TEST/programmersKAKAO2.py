def solution(n,t,m,p):
    result = "0"
    dic = {10: "A",11 : "B",12 : "C",13 : "D",14 : "E",15 : "F"}
    for i in range(m*t):
        mid = ""
        while i > 0:
            i , r = divmod(i,n)
            if r >= 10:
                r = dic[r]
            mid = str(r)+mid
        result += mid
        if len(result) >= m*t:
                break
    print(result)
    answer = ""
    for i in range(p-1,m*t,m):
        answer += result[i]
    return answer

print(solution(2,4,2,1))