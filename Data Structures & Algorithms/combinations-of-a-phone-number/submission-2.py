class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        keyMap = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z'],
        }

        ans = []

        def dfs(i,s):
            if i==len(digits):
                ans.append(s)
                return

            arr = keyMap[digits[i]]
            print(arr)
            for j in arr:
                dfs(i+1,s+j)

        if digits:
            dfs(0,"")
        print(ans)
        return ans