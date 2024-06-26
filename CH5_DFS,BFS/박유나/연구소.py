# from itertools import combinations
# answer=[]
# trash=[]
# #입력받기
# n, m = map(int, input().split())
# temp = [[0] * m for _ in range(n)] 
# institute = [list(map(int, input().split())) for _ in range(n)]


# for l in range(m):
#     trash.append(1)
# institute.insert(0,trash)
# institute.insert(n+1,trash)
# graph=institute.copy()
# print(graph)
# # #조합 설정.
# # nums=[]
# # for i in range(n):
# #     for j in range(m):
# #         if institute[i][j]==0: 
# #            nums.append((i, j))
# # num=list(combinations(nums,3))


# # #바이러스 감염시키기
# # def move(graph):
# #     for i in range(n):
# #         for j in range(m):
# #             if graph[i][j]==2:
# #                 if graph  
# #     pass



# # # 벽만들기
# # for i in range(len(num)):
# #     for j in range(3):
# #             graph[num[i][j][0],num[i][j][1]]=1
# #             move()
# #             graph.clear()
# #             graph=institute.copy()

# # result=max(answer)
# # print(result)



import sys; 
from itertools import combinations
import copy
sys.setrecursionlimit(100000)

empty_index=[]
virus_index=[]

N, M = map(int, input().split())
matrix_in=[]
for i in range(N):
    matrix_in.append(list(map(int, input().split())))
    for j in range(M):
        if matrix_in[i][j]==0:
            empty_index.append([i,j])
        if matrix_in[i][j]==2:
            virus_index.append([i,j])

check = [[0]*M for _ in range(N)]

# DFS 바이러스가 퍼지는 것을 구현
def dfs(matrix, ck, x, y):
    if ck[x][y] == 0:
        ck[x][y] = 1
        if matrix[x][y] == 0:
            matrix[x][y] = 2
        # dx, dy 하는 것 보다 if로 나누면 조금 더 수행시간이 빠릅니다.
        if x+1 < N and ck[x+1][y] == 0 and matrix[x+1][y] != 1:
            dfs(matrix, ck, x+1, y)
        if x-1 >= 0 and ck[x-1][y] == 0 and matrix[x-1][y] != 1:
            dfs(matrix, ck, x-1, y)
        if y-1 >= 0 and ck[x][y-1] == 0 and matrix[x][y-1] != 1:
            dfs(matrix, ck, x, y-1)
        if y+1 < M and ck[x][y+1] == 0 and matrix[x][y+1] != 1:
            dfs(matrix, ck, x, y+1)
    return matrix

result = 0
for coms in combinations(empty_index, 3):
 
    V_in = copy.deepcopy(matrix_in)
    cks = copy.deepcopy(check)
    
    # 벽세우기
    for i, j in coms:
        V_in[i][j] = 1

    # 바이러스 퍼뜨리기
    for i, j in virus_index:
        V_in = dfs(V_in, cks, i, j)

    # 안전지대 세기
    count=0
    for i in range(N):
        for j in range(M):
            if V_in[i][j]==0:
                count+=1

    result = max(result, count)

print(result)