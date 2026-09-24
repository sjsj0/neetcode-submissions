class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # n = len(flights)
        adj = {i:[] for i in range(len(flights))}

        if src>=len(adj) or dst>=len(adj):
            return -1

        for s, d, p in flights:
            if s<len(adj):
                adj[s].append((p, d))

        print(adj)

        distances = {i: float('inf') for i in range(len(adj))}
        distances[src] = 0
        print(distances)

        minHeap = [(0, src, -1)]
        # visited = set()
        # res = []

        while minHeap:
            print(minHeap)
            price, place, stops = heapq.heappop(minHeap)
            print(price, place, stops)

            if place == dst:
                return price

            if stops==k:
            #  or place in visited:
                continue
            
            # visited.add(place)

            for p, nei in adj[place]:
                print(f'node:{place}, nei:{nei}')
                # if nei not in visited:
                newPrice = price + p
                newStops = stops + 1
                # if newPrice < distances[nei]:
                distances[nei] = newPrice
                heapq.heappush(minHeap, (newPrice, nei, newStops))

        return -1
        #  if res==[] else min(res)