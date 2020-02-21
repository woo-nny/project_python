class Tree:
    def __init__(self,N):
        self.list = [0]*(N+1) #공간 형성
        self.N = N
        self.cnt = 1 #노드의 수
        self.numbering(1) #1번부터 넘버링
    def numbering(self,num):
        if num <= N:
            self.numbering(num*2) 
            self.list[num] = self.cnt
            self.cnt += 1
            self.numbering(num*2+1)
    def result(self):
        return ' '.join(map(str,(self.list[1],self.list[self.N//2])))

T = int(input())

for T in range(T):
    N = int(input())
    tree = Tree(N)
    print("#{} {}".format(T+1,tree.result()))