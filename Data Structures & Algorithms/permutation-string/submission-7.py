class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # my solution - O(n*log n) because of sorted..
        for i in range(len(s2)-len(s1)+1):
            substring = s2[i:i+len(s1)]
            if sorted(s1) == sorted(substring):
                return True
        return False

