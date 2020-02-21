question = [[5,2,1,1,9],
[3,3,8,3,1],
[9,2,8,8,6],
[1,5,7,8,3],
[5,5,4,6,8]]

INT_MAX = 10000

col_check = [False] * len(question)
min_sol = INT_MAX
length = len(question)

def solution(row,score,length):
    global min_sol

    if row == length:
        if score < min_sol:
            min_sol = score
        return min_sol
    
    for i in range(0,length):
        if col_check[i] == False:
            solution(row+1,score+question[row][i],length)
            col_check[i] = False
    return min_sol

print(solution(0,0,length))

