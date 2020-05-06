def make_tree(number1, number2, add):
    global Min
    global cnt
    number1_parents = union_find(number1)
    number2_parents = union_find(number2)
    print(number1_parents,number2_parents)
    print(parents_list)
    if number1_parents != number2_parents:
        number1, number2 = [number2, number1] if number1_parents > number2_parents else [number1, number2]
        parents_list[number2][0] = number1
        rank[number1] += 1
        parents_list[number2][1] = add
        Min += add
        cnt += 1

def union_find(number):
    if parents_list[number][0] == number:
        return parents_list[number][0]
    else:
        union_find(parents_list[number][0])


T = int(input())
for t in range(1,T+1):
    V, E = list(map(int, input().split()))
    problem = []
    for _ in range(E):
        problem.append(list(map(int, input().split())))
    problem.sort(key = lambda x:x[2])
    parents_list = []
    for i in range(0, V+1):
        parents_list.append([i,0])
    rank = [0]*(V+1)
    Min = 0
    cnt = 0
    for parents,child,add in problem:
        if cnt < V:
            make_tree(parents, child, add)
        else:
            break
    print(parents_list)
    print("#{} {}".format(t,Min))
    