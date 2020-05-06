def solution(numbers):
    for i in range(len(numbers)):
        if numbers[i] < 10:
            numbers[i] = [numbers[i]*1110,numbers[i]]
        elif numbers[i] < 100:
            q,r = divmod(numbers[i],10)
            if q <= r:
                numbers[i] = [(numbers[i]*10 + numbers[i]//10)*10 +1,numbers[i]]
            else:
                numbers[i] = [(numbers[i]*10 + numbers[i]//10)*10 -1,numbers[i]]
        elif numbers[i] < 1000:
            numbers[i] = [(numbers[i])*10,numbers[i]]
        else:
            numbers[i] = [1,numbers[i]]
    numbers.sort(key = lambda x : x[0],reverse = True)
    ans = ""
    for _,number in numbers:
        ans += str(number)
    if int(ans) == 0:
        ans = "0"
    return ans
numbers = [3, 30, 34, 5, 100,10,9,987,999,321,898,0,1000]
print(solution(numbers))