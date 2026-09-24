class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     if (endWord not in wordList) or (beginWord == endWord):
    #         return 0

    #     n = len(wordList)
    #     m = len(wordList[0])
    #     adj = [[] for _ in range(n)]
    #     mp = {}
    #     for i in range(n):
    #         mp[wordList[i]] = i

    #     ## making adj list
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             cnt = 0
    #             for k in range(m):
    #                 if wordList[i][k] != wordList[j][k]:
    #                     cnt += 1
                
    #             ## 2 words just differ by 1 char
    #             if cnt == 1:
    #                 adj[i].append(j)
    #                 adj[j].append(i)

        
    #     ## chking all the words in comparison to beginWord and storing it into queue
    #     queue = deque()
    #     visit = set()


    #     for i in range(m):
    #         for c in range(97,97+26):
    #             if chr(c) == beginWord[i]:
    #                 continue
                
    #             newWord = beginWord[:i] + chr(c) + beginWord[i+1:]

    #             # chk if new word is there in the wordList
    #             if newWord in mp and mp[newWord] not in visit:
    #                 visit.add(mp[newWord])
    #                 queue.append(mp[newWord])

    #     ## iterating the word now
    #     res = 1
    #     while queue:
    #         res+=1
    #         # inc at each level
    #         for i in range(len(queue)):
    #             wordNode = queue.popleft()

    #             if wordList[wordNode] == endWord:
    #                 return res
                
    #             for nei in adj[wordNode]:
    #                 if nei not in visit:
    #                     visit.add(nei)
    #                     queue.append(nei)

    #     return 0

    ## Optimised version
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0


        words = set(wordList)
        res = 0

        queue = deque()
        queue.append(beginWord)

        while queue:
            res+=1
            ## level by level traversal
            for _ in range(len(queue)):
                nodeWord = queue.popleft()

                if nodeWord == endWord:
                    return res

                for i in range(len(nodeWord)):
                    for c in range(97,97+26):
                        if chr(c) == nodeWord[i]:
                            continue
                        
                        probableNei = nodeWord[:i] + chr(c) + nodeWord[i+1:]
                        if probableNei in words:
                            queue.append(probableNei)
                            words.remove(probableNei)

        return 0
