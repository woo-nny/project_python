def mergeSeqLists():
    finalSeq = []

    finalSeq.extend(res[0])

    for idx in range(1, M):
        ptr = len(finalSeq)
        for i, num in enumerate(finalSeq):
            if res[idx][0] < num:
                ptr = i
                break

        finalSeq = finalSeq[:ptr] + res[idx] + finalSeq[ptr:]

    return finalSeq
T = int(input())

for T in range(T):
    N,M= map(int,input().split())
    res =[[int(num) for num in input().split()] for M in range(M)]
    ans = mergeSeqLists()
    print('#{} '.format(T+1), end='')
    print(' '.join(str(n) for n in ans[-1:-11:-1]))