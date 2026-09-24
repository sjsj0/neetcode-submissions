class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force -------------------------
        # ans=[0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     temp=0
        #     for j in range(i+1, len(temperatures)):
        #         temp+=1
        #         if temperatures[j]>temperatures[i]:
        #             ans[i] = temp
        #             break
        # return ans

        # Stack -------------------------
        ans = [0] * len(temperatures)
        stack=[]
        for i, t in enumerate(temperatures):
            print(stack)
            if stack:
                while stack and t > stack[-1][1]:
                    topOfStack = stack.pop()
                    ans[topOfStack[0]] = i - topOfStack[0]
                stack.append([i,t])
            else:
                stack.append([i,t])
        
        return ans