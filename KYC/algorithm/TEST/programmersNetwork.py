def solution(n,computer):
    row_parent = [i for i in range(n)]
    for i in range(n):
        row =[]
        i_parent = parents(i,row_parent)
        for j in range(n):
            if computer[i][j] ==1:
                row.append(j)
                j_parent = parents(j,row_parent)
                if j_parent < i_parent:
                    i_parent = j_parent
        for j in row:
            j_parent = parents(j,row_parent)
            row_parent[j_parent] = i_parent
    parent_list = []
    for i in range(n):
        parent_list.append(parents(i,row_parent))

    return len(set(parent_list))

def parents(j,parents_metrix):
    P = parents_metrix[j]
    if P == j:
        return P
    else:
        return parents(P,parents_metrix)




testcase1 = [[1,0,0,1],[0,1,1,1],[0,1,1,0],[1,1,0,1]]
testcase2 = [[1, 0, 0], [0, 1, 1], [1, 0, 1]]

print(solution(3,testcase2))