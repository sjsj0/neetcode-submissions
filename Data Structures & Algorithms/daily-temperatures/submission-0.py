class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            temp=0
            for j in range(i+1, len(temperatures)):
                temp+=1
                if temperatures[j]>temperatures[i]:
                    ans[i] = temp
                    break
            
        
        return ans