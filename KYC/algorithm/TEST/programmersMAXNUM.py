def solution(number, k):
    start = 1
    while k != 0:
        check = True
        for i in range(start,len(number)):
            if number[i-1] < number[i]:
                number = number[:i-1] + number[i:]
                k -= 1
                if i-1 <= 0:
                    start = 1
                else:
                    start = i - 1
                check = False
                break
        if check == True:
            number = number[:len(number)-k]
            break
    return number