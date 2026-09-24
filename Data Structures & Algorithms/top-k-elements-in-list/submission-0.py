class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)

        for n in nums:
            res[n]+=1

        sortedRes = dict(sorted(res.items(), key=lambda item:item[1], reverse=True))
        print(sortedRes.keys())
        return list(sortedRes.keys())[:k]