class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = {i:[] for i in range(numCourses)}
        for course, preq in prerequisites:
            preqMap[course].append(preq)


        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if preqMap[course] == []:
                return True

            visited.add(course)
            for pre in preqMap[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            # preqMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True