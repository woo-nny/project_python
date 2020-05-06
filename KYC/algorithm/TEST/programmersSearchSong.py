# class Query_info:

#     def __init__(self,query,index,num_question):
#         self.prev = None
#         self.query = query
#         self.index = [index]
#         self.num_question = num_question
#         self.next = None
#         self.other = None
# class Query_list:

#     def __init__(self,length):
#         self.root = None
#         self.length = length
#     def input_query(self,query,index,num_question):
#         self.root = self._input_query(self.root,query,index,num_question)

#     def _input_query(self, query_info, query, index, num_question):
#         if query_info == None:
#             query_info = Query_info(query,index, num_question)
#         else:
#             if query_info.query == query:
#                 query_info.index.append(index)
#             elif num_question < query_info.num_question:
#                 for_ran = range(self.length) if query[0] == '?' else range(self.length+1,-1,-1)
#                 for i in for_ran:
#                     if query_info.query[i] == '?' and query[i].isalpha():
#                         query_info.next.append(self._input_query(query))


# def solution(words,queries):
#     words = set(words)
#     queries_length = len(queries)
#     answer = [0]*queries_length

#     dic_query = {}
#     for i in range(len(queries)):
#         query = queries[i]
#         n = len(query)
#         if n in dic_query.keys():
#             append = True
#             for j in range(len(dic_query[n])):
#                 if dic_query[n][j][0] == query:
#                     dic_query[n][j].append(i)
#                     append=False
#                     break
#             if append == True:
#                 dic_query[n].append([query,i])
#         else:
#             dic_query[n] = [[query,i]]

#     for word in words:
#         len_word = len(word)
        
#         if len_word in dic_query.keys():    
#             for query_info in dic_query[len_word]:
#                 for_range = range(len_word-1,-1,-1) if query_info[0][0] == '?' else range(len_word)
#                 check_append = True

#                 for i in for_range:
#                     if query_info[0][i] != '?' and word[i] != query_info[0][i]:
#                         check_append = False
#                         break
#                     elif query_info[0][i] == '?':
#                         break

#                 if check_append == True:
#                     for ind in query_info[1:]:
#                         answer[ind] += 1

#     return answer




class Trie:
    
    def __init__(self,length):
        self.root = {}
        self.root['normal'] = {'count':0}
        self.root['reverse'] = {'count':0}
        self.length = length

    def insert(self, s):
        n_cur = self.root['normal']
        r_cur = self.root['reverse']
        r_s = s[::-1]

        while s:
            n_cur['count'] += 1
            r_cur['count'] += 1
            if s[0] not in n_cur: n_cur[s[0]] = {'count':0}
            if r_s[0] not in r_cur: r_cur[r_s[0]] = {'count':0}
            n_cur = n_cur[s[0]]
            r_cur = r_cur[r_s[0]]
            s = s[1:]
            r_s = r_s[1:]

    def count(self, s):
        if s == '?'*self.length:
            return self.root['reverse']['count']
        elif s[0] == '?':
            cur = self.root['reverse']
            s = s[::-1]
        else:
            cur = self.root['normal']
        while s:
            if s[0] == '?': return cur['count']
            elif s[0] not in cur : return 0
            else:
                cur = cur[s[0]]
                s=s[1:]
        return cur['count']
                

def solution(words,queries):
    len_queries = len(queries)
    answer = [0]*len_queries
    trie = {}
    for word in words:
        length = len(word)
        try:
            trie[length].insert(word)
        except:
            trie[length] = Trie(length)
            trie[length].insert(word)
    
    for i in range(len_queries):
        query = queries[i]
        try:
            answer[i] = trie[len(query)].count(query)
        except:
            None  
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao","forst"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))

