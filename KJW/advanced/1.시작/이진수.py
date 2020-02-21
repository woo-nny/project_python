sixteen = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9,
        'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}
T = int(input())
for T in range(T):
    N, num = map(str,input().split())
    res1 = ''
    for i in num:
        res2 =''
        mok, nam = 0,0
        six_num=sixteen[i]
        for j in range(4):
            mok = six_num//2
            nam = six_num%2
            res2 =str(nam)+ res2
            six_num =mok
        res1 += res2
    print("#{} {}".format(T+1,res1))



# T = int(input())
# for T in range(T):
#     num, data = input().split()
#     result = ''
#     for i in range(int(num)):
#         result += '{:04b}'.format(int(data[i], 16)) # 한글자씩 16진수를 2진수 4자리로
#     print('#{} {}'.format(T+1, result))
