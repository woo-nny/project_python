def BackTraking(now_position,visit_number,battery):
    global Min
    global destination
    battery = bus_stop[now_position]#베터리가 누적되지 않아야함
    if Min != 1:
        if now_position + battery >= destination:
            if visit_number < Min:
                Min = visit_number
                return
            else:
                return
        elif visit_number > Min:
            return
        else:
            for i in range(battery,0,-1):
                BackTraking(now_position + i,visit_number+1,battery - i)
    else:
        return
def min_bus_stop():
    BackTraking(0,0,0)
T = int(input())
for t in range(1,T+1):
    question = list(map(int, input().split()))
    N, bus_stop = question[0], question[1:]
    destination = N - 1
    Min = N
    min_bus_stop()
    print("#{} {}".format(t,Min))