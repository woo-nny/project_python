num = int(input())
a = []
count = 0

for i in range(1,num+1):
    if(num%i==0):
        print("{}(은)는 {}의 약수입니다.".format(i,num))
        a.append(i)
        count += 1
if(count ==2):
    print("{}(은)는 {}과 {}로만 나눌 수 있는 소수입니다.".format(num,a[0],a[1]))