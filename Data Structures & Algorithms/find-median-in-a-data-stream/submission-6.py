class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        if n%2 == 1:
            return self.data[n//2]
        else:
            return (self.data[n//2 -1] + self.data[n//2])/2









    # ## Max Heap --------------------------------
    # def __init__(self):
    #     self.maxHeap, self.minHeap = [], []

    # def addNum(self, num: int) -> None:
    #     if self.maxHeap and num > self.maxHeap[0]:
    #         heapq.heappush(self.maxHeap, num)
    #     else:
    #         heapq.heappush(self.minHeap, -num)

    #     # ## either this or this --
    #     # if self.minHeap and -num > self.minHeap[0]:
    #     #     heapq.heappush(self.minHeap, -num)
    #     # else:
    #     #     heapq.heappush(self.maxHeap, num)


    #     ## Balancing the no in heap, if unbalanced move from one to the another
    #     if len(self.minHeap) > len(self.maxHeap) + 1:
    #         val = -1 * heapq.heappop(self.minHeap)
    #         heapq.heappush(self.maxHeap, val)
    #     if len(self.maxHeap) > len(self.minHeap) + 1:
    #         val = heapq.heappop(self.maxHeap)
    #         heapq.heappush(self.minHeap, -val)


    # def findMedian(self) -> float:
    #     if len(self.minHeap) > len(self.maxHeap):
    #         return -self.minHeap[0]
    #     elif len(self.maxHeap) > len(self.minHeap):
    #         return self.maxHeap[0]
    #     else:
    #         return (-self.minHeap[0] + self.maxHeap[0])/2
        