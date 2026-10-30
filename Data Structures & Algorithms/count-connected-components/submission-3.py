class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=set()
        
        def dfs(node):
            visit.add(node)

            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
            return 

        

        components=0
        for i in range(n):
            if i not in visit:
                components+=1
                dfs(i)
        
        return components
            