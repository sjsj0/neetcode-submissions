class Solution:

    # ## BFS (Kahn's algo)
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     inDegree = [0] * numCourses
    #     adj = [[] for _ in range(numCourses)]
    #     for course,preq in prerequisites:
    #         inDegree[course] += 1
    #         adj[preq].append(course)

    #     queue = deque()

    #     for c in range(numCourses):
    #         if inDegree[c] == 0:
    #             queue.append(c)

    #     finish = []
    #     while queue:
    #         c = queue.popleft()
    #         finish.append(c)

    #         for nei in adj[c]:
    #             inDegree[nei] -= 1
    #             if inDegree[nei] == 0:
    #                 queue.append(nei)

    #     return finish if len(finish) == numCourses else []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqMap = {i:[] for i in range(numCourses)}
        for course, preq in prerequisites:
            preqMap[course].append(preq)

        output = []
        cycle = set()
        visited = set()

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True


            cycle.add(course)
            for pre in preqMap[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            # preqMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output
