class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)
        
        while len(stones)>1:
            top = heapq.heappop(stones)
            second = heapq.heappop(stones)
            print(f'top:{top}, second:{second}')

            if top < second:
                diff = second-top
                heapq.heappush(stones, -diff)
            print(stones)          

        stones.append(0)
        return abs(stones[0])