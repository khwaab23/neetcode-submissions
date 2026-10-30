class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)

        for src,dst in edges:
            adj[src].append(dst)

        visited=set()
        path=set()
        topsort=[]

        
    
        def dfs(src):
            if src in visited:
                return True
            if src in path:
                return False
            
            
            path.add(src)

            for nei in adj[src]:
                if not dfs(nei):
                    return False
            
            path.remove(src)
            visited.add(src)
            topsort.append(src)
            return True

        for i in range(n):
            if not dfs(i):
                return []
        topsort.reverse()
        return topsort

        