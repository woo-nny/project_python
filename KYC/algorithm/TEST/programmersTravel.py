def solution(tickets):
    start= "ICN"
    result_list = ["ICN"]
    length = len(tickets)
    check_list = [False]*length
    dfs(tickets,start,result_list,length,check_list)
    return result

def dfs(tickets,start,result_list,length,check_list):
    global result
    if len(result_list) == length+1:
        result = result_list
        return 1
    elif len(result) < length+1:
        comple = []
        for i in range(length):
            if tickets[i][0] == start and check_list[i]==False:
                comple.append([tickets[i][1],i])
        
        if len(comple) != 0:
            comple.sort()
            for start,i in comple:
                check_list[i]=True
                A = dfs(tickets,start,result_list+[start],length,check_list)
                if A == None:
                    check_list[i] = False
result = []
tickets = [['ICN', 'COO'], ['ICN', 'BOO'], ['COO', 'ICN'], ['BOO', 'DOO']]
tickets2 = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(tickets))



# def solution(tickets):
#     def helper(tickets, route):
#         if tickets == []:
#             return route
#         left = [i for i in range(len(tickets)) if tickets[i][0] == route[-1]]
#         if left == []:
#             return None
#         left.sort(key = lambda i: tickets[i][1])

#         for next in left:
#             rest = helper(tickets[:next]+tickets[next+1:], route+[tickets[next][1]])
#             if rest is not None:
#                 return rest
#     return helper(tickets, ["ICN"])