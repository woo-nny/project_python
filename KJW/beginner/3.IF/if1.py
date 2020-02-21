num = int(input())

for i in range(1,num+1):
    if (num%i ==0):
        print("{}(은)는 {}의 약수입니다.".format(i,num))