class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        path=set()
        visit=set()
        
        def dfs(crs):
            if crs in path:
                return False
            
            if crs in visit:
                return True
            
            path.add(crs)
            visit.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            path.remove(crs)
            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

            


        
