def binary_search(A_list,find_number,check):
    l = 0
    r = len(A_list) - 1
    while True:
        m = (l+r) // 2
        middle = A_list[m]
        if find_number == middle:
            return 1
        elif find_number < middle:
            if check == "left":
                return 0
            else:
                check = "left"
                r = m - 1
        elif find_number > middle:
            if check == "right":
                return 0
            else:
                check = "right"
                l = m + 1
def search(A,B):
    cnt = 0
    for i in B:
        cnt += binary_search(A,i,"None")
    return cnt

T = int(input())
for t in range(1,T+1):
    N,M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    print("#{} {}".format(t, search(A,B)))