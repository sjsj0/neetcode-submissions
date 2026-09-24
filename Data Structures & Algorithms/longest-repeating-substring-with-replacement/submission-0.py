class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap=defaultdict(int)
        l=0
        r=1
        maxLength=0

        for i,c in enumerate(s):
            hashMap[c]+=1
            
            print(f'max in hashMap: {max(hashMap.values())}, r:{r}, l:{l}')
            if (r-l) - max(hashMap.values()) > k:
                hashMap[s[l]]-=1
                l+=1
                print(f'l:{l}')
            maxLength = max(maxLength, r-l)
            r+=1

        return maxLength
