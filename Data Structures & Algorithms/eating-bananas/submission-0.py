class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans = r
        while l<=r:
            rate = (l+r) // 2
            print(f'rate:{rate}')
            totalTime = sum([-(-p//rate) for p in piles])

            if totalTime <= h:
                ans = min(ans, rate)
                r = rate - 1
            elif totalTime > h:
                l = rate + 1

            print(ans)

        return ans