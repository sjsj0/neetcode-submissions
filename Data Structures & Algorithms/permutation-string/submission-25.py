class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # my solution - O(n*log n) because of sorted..
        # for i in range(len(s2)-len(s1)+1):
        #     substring = s2[i:i+len(s1)]
        #     if sorted(s1) == sorted(substring):
        #         return True
        # return False

        ## my solution - messy one but sliding window..
        if len(s1)>len(s2):
            return False

        s1HashMap = defaultdict(int)
        windowHashMap = defaultdict(int)
        for i in range(len(s1)):
            s1HashMap[s1[i]] += 1
            windowHashMap[s2[i]] += 1

        # count=0
        # for k in s1HashMap:
        #     if s1HashMap[k] == windowHashMap[k]:
        #         count += s1HashMap[k]
        # if count == len(s1):
        #     return True

        for i in range(len(s2)-len(s1)+1):
            if i>0:
                windowHashMap[s2[i-1]] -= 1
                windowHashMap[s2[i+len(s1)-1]] += 1

            count=0
            for k in s1HashMap:
                if s1HashMap[k] == windowHashMap[k]:
                    count += s1HashMap[k]
            if count == len(s1):
                return True


        return False

        # cleaner version of the same above sol..




            