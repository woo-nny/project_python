a =[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

#while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
count =0
sum = 0
while count<len(a):
    for i in range(0,len(a)):
        if a[i]>=80:
            sum +=a.pop(i)
    count +=1
print(sum)
