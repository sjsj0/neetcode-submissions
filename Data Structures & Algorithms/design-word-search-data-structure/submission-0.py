class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            curr = node

            for i in range(index, len(word)):
                c = word[i]

                ## DFS logic to search for each child
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                
                ## the same usual logic for char by char search and moving fwd
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.endOfWord


        return dfs(0, self.root)
            
