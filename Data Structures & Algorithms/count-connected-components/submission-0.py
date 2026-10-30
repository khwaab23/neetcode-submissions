class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        adj={i:[] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited=set()
        def dfs(i):
            if i in visited:
                return True
            
            visited.add(i)
            for next1 in adj[i]:
                dfs(next1)
        

        count=0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i,)
        
        return count
