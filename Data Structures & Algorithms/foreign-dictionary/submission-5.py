class Solution:

    # ## DFS --------------------------------------------
    # def foreignDictionary(self, words: List[str]) -> str:
    #     adj = {c: set() for w in words for c in w}

    #     n = len(words)
    #     for i in range(n-1):
    #         w1,w2 = words[i], words[i+1]

    #         minLen = min(len(w1), len(w2))
    #         if len(w1)>len(w2) and w1[:minLen] == w2[:minLen]:
    #             return ""

    #         for j in range(minLen):
    #             if w1[j]!=w2[j]:
    #                 adj[w1[j]].add(w2[j])
    #                 break

    #     visited = {}
    #     res = []

    #     def dfs(char):
    #         if char in visited:
    #             return visited[char]

    #         visited[char] = True

    #         for nei in adj[char]:
    #             if dfs(nei):
    #                 return True

    #         visited[char] = False
    #         res.append(char)

    #     for char in adj:
    #         if dfs(char):
    #             return ""


    #     res.reverse()
    #     return ''.join(res)

    ## Kahn's algorithm ---------------------------------------
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        inDegree = {c:0 for c in adj}

        n = len(words)
        for i in range(n-1):
            w1,w2 = words[i], words[i+1]

            minLen = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inDegree[w2[j]] += 1
                    break

        res = []
        queue = deque()
        for c in inDegree:
            if inDegree[c] == 0:
                queue.append(c)

        while queue:
            char = queue.popleft()
            res.append(char)

            for nei in adj[char]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)

        if len(res) != len(inDegree):
            return ""

        return ''.join(res)