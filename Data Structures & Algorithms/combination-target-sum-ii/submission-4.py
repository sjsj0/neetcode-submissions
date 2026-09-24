class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, temp, total):
            if total == target:
                if temp not in res:
                    res.append(temp.copy())
            if i >= len(candidates):
                return



            temp.append(candidates[i])
            dfs(i+1, temp, total+candidates[i])    
            temp.pop()
            dfs(i+1, temp, total)

        dfs(0,[],0)

        return res
