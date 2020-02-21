T = int(input())
for T in range(T):
    num = float(input())
    result = ''
    for i in range(1, 13):
        num *= 2
        result += str(int(num) % 2) # 1의 자리
        if num % 1 == 0: # 소수점
            break
    else:
        result = 'overflow'
    print('#{} {}'.format(T+1, result))
