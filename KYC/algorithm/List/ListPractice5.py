
def jinbeob(n):
    if n > 1:
        q,r = divmod(n,2)
        return jinbeob(q)+str(r)
    else :
        return str(n)


arr = [1,6,2,5,8]
for i in range(1 << len(arr)): # 여기서 2진수로된 구성을 만들어내고 00001이상 100000미만까지 모두 나옴
    for j in range(len(arr)):
        if i & (1<<j):#여기서 1<<j는 00001,00010,00100,01000,10000과 같은 자리를 나타냄, i와 비교해 존재하면 1이될것임.
            print(arr[j],end=",") #& 자체가 비트연산이므로 실제로는 숫자 값으로 나오지만, 이진수변환된 자리를 비교해줌
    print()
