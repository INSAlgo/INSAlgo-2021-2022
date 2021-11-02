import sys
N = int(input())  # number of nodes
adj = [[] for _ in range(N)]
for i in range(1, N):
    c, p = map(int,input().split())
    adj[p].append(c)
scores = [[0, 0, 0] for _ in range(N)]
#Each node get 3 scores : [A, B, C]
#A -> Max score reachable if the node is not taken
#B -> Max score reachable if the node is taken but no children is taken
#C -> Max score reachable if the node is taken and one children is taken
def calc_score(adj, current_id, computed_scores):
    if len(adj[current_id])==0:
        computed_scores[current_id]=[0,1,0]
        return
    else:
        for child in adj[current_id]:
            calc_score(adj,child,computed_scores)
            #Score A is the sum of the max score of each child
            computed_scores[current_id][0]+=max(computed_scores[child])
            #Score B is the sum of score A for each child plus one
            computed_scores[current_id][1]+=computed_scores[child][0]
        computed_scores[current_id][1] += 1
        #Initialize score C by taking the score B of itself, and substracting score A of one child and adding score B of the same child
        computed_scores[current_id][2]=computed_scores[current_id][1]-computed_scores[adj[current_id][0]][0]+computed_scores[adj[current_id][0]][1]
        #Choose the max score C by repeating the process for each child
        for child in adj[current_id]:
            computed_scores[current_id][2]=max(computed_scores[current_id][2],computed_scores[current_id][1]-computed_scores[child][0]+computed_scores[child][1])
        return
calc_score(adj,0,scores)
print(max(scores[0]))
