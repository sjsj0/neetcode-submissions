class Solution:

    # ## DFS (cycle detection) ---------------------------
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     preqMap = {i:[] for i in range(numCourses)}
    #     for course, preq in prerequisites:
    #         preqMap[course].append(preq)


    #     visited = set()

    #     def dfs(course):
    #         if course in visited:
    #             return False
            
    #         if preqMap[course] == []:
    #             return True

    #         visited.add(course)
    #         for pre in preqMap[course]:
    #             if not dfs(pre):
    #                 return False
            
    #         visited.remove(course)
    #         # preqMap[course] = []
    #         return True

    #     for c in range(numCourses):
    #         if not dfs(c):
    #             return False

    #     return True

    ## Kahn algo (topological sort) -------------------------------------
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src,dst in prerequisites:
            inDegree[src] += 1
            adj[dst].append(src)


        queue = deque()
        for c in range(numCourses):
            if inDegree[c] == 0:
                queue.append(c)


        finish=0
        while queue:
            c = queue.popleft()
            finish += 1
            for nei in adj[c]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)


        return finish == numCourses


