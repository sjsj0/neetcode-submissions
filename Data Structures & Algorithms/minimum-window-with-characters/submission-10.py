class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        if len(s)<len(t):
            return ""

        ans=[]
        tHashMap = {}
        for c in t:
            tHashMap[c] = 1 + tHashMap.get(c,0)
        
        print(tHashMap)

        windowHashMap = {}
        l=r=0
        for i,c in enumerate(s):
            if c in t:
                windowHashMap[c] = 1+ windowHashMap.get(c,0)
                # windowHashMap = {k:v for k,v in windowHashMap.items() if v!= 0}

            # if tHashMap.keys() == windowHashMap.keys():
            if all(windowHashMap.get(k, 0) >= v for k, v in tHashMap.items()):
                print(s[l:r+1])
                ans.append(s[l:r+1])
                windowHashMap[s[l]] -= 1
                windowHashMap = {k:v for k,v in windowHashMap.items() if v!= 0}
                l+=1
                while l<len(s):
                    if s[l] not in t:
                        l+=1
                    elif s[l] in t and all(windowHashMap.get(k, 0) >= v for k, v in tHashMap.items()):
                        print(s[l:r+1])
                        ans.append(s[l:r+1])
                        windowHashMap[s[l]] -= 1
                        windowHashMap = {k:v for k,v in windowHashMap.items() if v!= 0}
                        l+=1
                    else:
                        break


            if not windowHashMap:
                l+=1

            print(f'windowHashMap:{windowHashMap} | l:{l} | r:{r} | c:{c}')
            r+=1
        print(f'ans:{ans}')
        if not ans:
            return ""
        else:
            return min(ans, key=len)

