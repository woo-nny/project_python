def solution(s):
    min = len(s)
    s_number = len(s)//2+1
    while s_number != 1:
        s_number -= 1
        result = len(s)
        comp_num = 1
        check = s[:s_number]
        for i in range(s_number,len(s)+1,s_number):
            if check == s[i:i+s_number]:
                comp_num += 1
                result -= s_number
            elif check != s[i:i+s_number] or i == len(s):
                check = s[i:i+s_number]
                if comp_num != 1:
                    result += len(str(comp_num))
                comp_num = 1
            
        if result < min:
            min = result

    return min



s = "xababcdcdababcdcd"
print(solution(s))
