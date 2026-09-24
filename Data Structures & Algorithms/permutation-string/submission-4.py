class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            print(f'i:{i}, sorted(s1):{sorted(s1)}, sorted(s2[i:i+len(s1):{sorted(s2[i:i+len(s1)])}')
            if sorted(s1) == sorted(s2[i:i+len(s1)]):
                return True
        return False