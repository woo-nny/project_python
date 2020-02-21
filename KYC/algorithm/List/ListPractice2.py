#import sys input보다 빠르다고들 한다
#T = int(sys.stdin.readline())
T = int(input())
for a in range(1,T+1):
    #N = int(sys.stdin.readline())
    N = int(input())
    lis = list(map(int, input().split()))
    print("#{} {}".format(a,max(lis)-min(lis)))
