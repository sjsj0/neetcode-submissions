class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1                 ## minimum eating rate possible
        r=max(piles)        ## maximum eating rate required
        ans = r

        # lets binary search the eating rate and store the rate giving min totalTime
        while l<=r:
            rate = (l+r) // 2
            print(f'rate:{rate}')
            totalTime = sum([-(-p//rate) for p in piles])  ## -(-p//rate) way to calculate ceil..

            if totalTime <= h:
                ans = min(ans, rate)
                r = rate - 1
            elif totalTime > h:
                l = rate + 1

            print(ans)

        return ans