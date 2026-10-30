class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        for pre,crs in prerequisites:
            adj[crs].append(pre)
        
        def bfs(pre,crs):
            q=deque()
            q.append(crs)
            visit=set()
            visit.add(crs)
            while q:
                course=q.popleft()
                if course==pre:
                    return True
                
                for nei in adj[course]:
                    if nei in visit:
                        continue
                    
                    q.append(nei)
                    visit.add(nei)
            
            return False

        
        res=[]    
        for pre, crs in queries:
            if bfs(pre,crs):
                res.append(True)
            else:
                res.append(False)
        
        return res