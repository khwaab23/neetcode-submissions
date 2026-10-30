class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses=defaultdict(list)

        for pre in prerequisites:
            courses[pre[0]].append(pre[1])
        visited=set()
        def dfs(i):
            if i in visited:
                return False

            if courses[i]==[]:
                return True

            visited.add(i)
            for j in courses[i]:
                if not dfs(j):
                    return False
            visited.remove(i)
            courses[i]=[]
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True