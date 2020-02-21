from sys import stdin
T = int(stdin.readline())
for a in range(1,T+1):
   N = int(stdin.readline())
   lis = list(map(int, stdin.readline().strip()))
   mid = 0
   cnt = 0
   for b in set(lis): # 중복된 숫자를 제거해 검사해야할 숫자집단을 만든다.
       if cnt <= lis.count(b): #숫자 집단에서 나온 숫자를 lis에서 몇 개 있는지 카운트한다.
           cnt = lis.count(b)
           if mid < b:
               mid = b
   print("#{} {} {}".format(a,mid,cnt))

# dictionary

from sys import stdin    
T = int(stdin.readline())
for a in range(1,T+1):
    N = int(stdin.readline())
    val = list(map(int, stdin.readline().strip()))
    dic_val = sorted(set(val))
    key = list(map(lambda x : val.count(x), dic_val))
    dic = dict(zip(key,dic_val))
    print("#{}".format(a),max(dic),dic[max(dic)])

# 

from sys import stdin    
T = int(stdin.readline())
for a in range(1,T+1):
    N = int(stdin.readline())
    val = sorted(list(map(int, stdin.readline().strip())))
    max = 0
    numb = 0
    for b in sorted(set(val)):
        cnt = 0
        for c in range(0,len(val)):
            if b == val[0]:
                val.pop(0)
                cnt += 1
            else:
                max = cnt if cnt > max else max
                numb = b if max == cnt else numb
    
    print("#{}".format(a),max,numb)
        