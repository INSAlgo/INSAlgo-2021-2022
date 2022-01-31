class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False for _ in range(n)]
        adj=[[] for _ in range(n)]
        if source==destination:
            return True
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
        
        
        stack = [source]
        
        while stack:
            currentNode=stack.pop()
            if visited[currentNode]:
                continue
            visited[currentNode]=True
            
            for nei in adj[currentNode]:
                if nei==destination:
                    return True
                if not visited[nei]:
                    stack.append(nei)
        else:
            return False
        
