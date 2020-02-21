
count1 = 7
count2 = 0
while count1 >0:
    if count1%2 != 0:
        print(' '*count2,end='')
        print('*'*count1)
        count2 += 1
    if count1%2 ==0:
        print()
    count1 -= 1
