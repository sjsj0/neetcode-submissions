class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''

        for s in strs:
            # tempData=str(len(s))+'#'
            res=res+'#-#'+s
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=s.split('#-#')

        print(res[1:])
        return res[1:]
