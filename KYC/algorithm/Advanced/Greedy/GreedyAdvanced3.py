def babygin(player):
    cnt = 0
    lis=[0]*12
    for i in player:
        cnt += 1
        lis[i] +=1
        if lis[i] == 3:
            cnt -= 1
            break
        if i >= 2 and( 0 not in lis[i-2:i+1] or 0 not in lis[i-1:i+2] or 0 not in lis[i:i+3]):
            cnt -= 1
            break
        elif i == 1 and( 0 not in lis[i-1:i+2] or 0 not in lis[i:i+3]):
            cnt -= 1
            break
        elif i == 0 and 0 not in lis[i:i+3]:
            cnt -= 1
            break
    return cnt
T = int(input())
for t in range(1,T+1):
    card = list(map(int,input().split()))
    player_1, player_2 = [], []
    for i in range(len(card)):
        player_1.append(card[i]) if i % 2 == 0 else player_2.append(card[i])
    ans1 = babygin(player_1)
    ans2 = babygin(player_2)
    if ans1 > ans2:
        print("#{} {}".format(t,2))
    elif ans1 == ans2 == 6:
        print("#{} {}".format(t,0))
    else:
        print("#{} {}".format(t,1))