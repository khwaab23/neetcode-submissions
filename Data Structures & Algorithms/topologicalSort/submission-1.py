class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)

        
        topsort=[]
        visit=set()
        path=set()


        def dfs(src):
            if src in visit:
                return True
            if src in path:
                return False
            
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            visit.add(src)
            topsort.append(src)
            path.remove(src)
            return True
            


        for i in range(n):
            if not dfs(i):
                return []
        topsort.reverse()
        return topsort
