class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
            
        adj=defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visit=set()

        def dfs(src, prev):
            if src in visit:
                return False
            
            visit.add(src)
            for nei in adj[src]:
                if nei == prev:
                    continue
                if not dfs(nei, src):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visit) == n